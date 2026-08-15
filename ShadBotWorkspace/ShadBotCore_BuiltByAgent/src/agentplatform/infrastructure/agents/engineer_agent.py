from subprocess import Popen, PIPE, run
from typing import List

class EngineerAgent:
    """
    Infrastructure layer for the Engineer Agent.
    
    This class provides methods to interact with various I/O operations,
    such as filesystem, HTTP requests, subprocess calls, and database access.
    """

    def __init__(self):
        pass

    def read_file(self, file_path: str) -> str:
        """
        Read a file from the filesystem.

        :param file_path: Path to the file to be read.
        :return: Content of the file as a string.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except IOError as e:
            print(f"Error reading file {file_path}: {e}")
            return ""

    def write_file(self, file_path: str, content: str) -> None:
        """
        Write content to a file in the filesystem.

        :param file_path: Path to the file where the content will be written.
        :param content: Content to be written to the file.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")

    def run_subprocess(self, command: List[str]) -> str:
        """
        Run a subprocess with the given command.

        :param command: Command list to be executed.
        :return: Output of the subprocess execution.
        """
        try:
            result = run(command, check=True, capture_output=True, encoding='utf-8', errors='replace')
            return result.stdout
        except Exception as e:
            print(f"Error running subprocess: {e}")
            return ""

    def make_http_request(self, url: str) -> str:
        """
        Make an HTTP GET request to the given URL.

        :param url: URL to make the request to.
        :return: Response content as a string.
        """
        try:
            response = Popen(['curl', '-s', url], stdout=PIPE, stderr=PIPE)
            output, error = response.communicate()
            if response.returncode != 0:
                print(f"Error making HTTP request: {error.decode('utf-8')}")
                return ""
            return output.decode('utf-8')
        except Exception as e:
            print(f"Error running subprocess for HTTP request: {e}")
            return ""

    def connect_to_database(self, database_url: str) -> None:
        """
        Connect to a database using the provided URL.

        :param database_url: URL of the database to connect to.
        """
        raise NotImplementedError("Database connection is not implemented.")

# Example usage
if __name__ == "__main__":
    engineer_agent = EngineerAgent()
    content = engineer_agent.read_file('example.txt')
    print(content)
    engineer_agent.write_file('output.txt', 'Hello, World!')
    subprocess_output = engineer_agent.run_subprocess(['ls', '-l'])
    print(subprocess_output)
    http_response = engineer_agent.make_http_request('https://api.github.com')
    print(http_response)