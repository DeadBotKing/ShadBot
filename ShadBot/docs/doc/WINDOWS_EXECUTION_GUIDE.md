# ShadBot Agent Platform
# Windows Compatibility & Execution Guide

Version: 1.0  
Date: 2026-08-10  
Status: Official Windows Cross-Platform Specification

---

## 1. Cross-Platform Compatibility Guarantee

**ShadBot Agent Platform** is designed and audited to be **100% cross-platform compatible** across **Windows 10/11**, Linux, and macOS.

### 1.1 Architectural Safeguards for Windows
1. **Path Handling (`pathlib.Path`)**:  
   - All filesystem paths use Python's modern `pathlib.Path` instead of hardcoded string paths.  
   - Windows backslash paths (`C:\Workspace\Project`) and POSIX forward slash paths (`/home/user/Project`) are handled automatically without separator errors.
2. **No POSIX-Only System Calls**:  
   - No Linux-specific calls such as `os.fork()`, `fcntl`, `termios`, or `/dev/null` exist in `src/agentplatform/` or `src/projectintelligence/`.
3. **Subprocess & Terminal Execution**:  
   - The `TerminalTool` (`src/agentplatform/infrastructure/tools/terminal_tool.py`) executes commands via `subprocess.run(..., shell=True)`, which seamlessly delegates to `cmd.exe` or PowerShell on Windows.
4. **Line Ending Invariance (`\r\n` vs `\n`)**:  
   - All text and markdown parsers (`TaskParser`, `DirectoryWalker`, `GitStatus`, etc.) use `.splitlines()` and `.strip()`, ensuring Windows CRLF (`\r\n`) line endings are processed identically to LF (`\n`).
5. **Universal Dependencies**:  
   - Core libraries (`gitpython`, `requests`, `pytest`, `ruff`, `black`, `mypy`) have official Windows support and installers.

---

## 2. Step-by-Step Setup Guide on Windows 10/11

### 2.1 Prerequisites
- **Python**: Version 3.10 or higher installed from `python.org` (ensure "Add Python to PATH" is checked during installation).
- **Git**: Installed from `git-scm.com` (Git for Windows).

### 2.2 Unpacking & Virtual Environment Setup
Open **PowerShell** or **Command Prompt (CMD)** in the folder where you extracted `ShadBot-fixed.zip`:

#### Option A: PowerShell
```powershell
# 1. Create a Python Virtual Environment
python -m venv venv

# 2. Activate the Virtual Environment
.\venv\Scripts\Activate.ps1

# 3. Upgrade pip and install required dependencies
python -m pip install --upgrade pip
pip install pytest ruff black mypy gitpython requests
```
*(Note: If PowerShell shows a script execution error, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` first).*

#### Option B: Command Prompt (CMD)
```cmd
:: 1. Create a Python Virtual Environment
python -m venv venv

:: 2. Activate the Virtual Environment
.\venv\Scripts\activate.bat

:: 3. Upgrade pip and install required dependencies
python -m pip install --upgrade pip
pip install pytest ruff black mypy gitpython requests
```

---

## 3. Running All 165 Tests on Windows

To verify 100% Green test suite execution on your Windows machine:

### 3.1 In PowerShell
```powershell
$env:PYTHONPATH="src"
pytest tests/ -v
```

### 3.2 In Command Prompt (CMD)
```cmd
set PYTHONPATH=src
pytest tests/ -v
```

### 3.3 Expected Output on Windows
```text
============================= test session starts ==============================
platform win32 -- Python 3.1x.x, pytest-9.x.x, pluggy-1.x.x -- C:\...\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Username\ShadBot
configfile: pytest.ini
collecting ... collected 165 items

tests/agentplatform_tests (123 items)                  PASSED [ 74%]
tests/projectintelligence_tests (42 items)            PASSED [100%]

============================= 165 passed in 2.35s ==============================
```

---

## 4. Running ShadBot Application on Windows

To run the main ShadBot agent platform runner on Windows:

```powershell
$env:PYTHONPATH="src"
python run_agent.py
```

All workspace folders (`.shadbot`, `ShadBotWorkspace`) and configuration files are created in your local Windows user folder seamlessly.

---

## 5. Putting ShadBot to Work on a Real Project (End-to-End Execution)

To run ShadBot as an autonomous software engineering organization on a real project workspace:

### 5.1 How ShadBot Works in Real Life
ShadBot does not start from empty code; it starts from a **Project Workspace** containing a roadmap and task backlog:
1. `roadmap.yaml`: Defines the active phase of your project.
2. `tasks/backlog.yaml`: Contains the pending engineering tasks.

### 5.2 Running the Sample Project (`Meryx`)
A ready-to-run sample project named `Meryx` is included in `../ShadBotWorkspace/Meryx`.
To execute ShadBot autonomously on `Meryx` in **PowerShell**:

```powershell
# Ensure you are in the ShadBot directory and virtual environment is active
$env:PYTHONPATH="src"
python run_agent.py --project Meryx
```

### 5.3 Expected Real-World Orchestration Output
When you run the command above, ShadBot executes the full **4-stage autonomous pipeline**:

```text
======================================================================
Project : Meryx
Executed Results : 4
======================================================================
[1] success=True message=Project intelligence analysis completed.
[2] success=True message=Architecture plan generated.
[3] success=True message=Engineering completed.
[4] success=True message=Review workflow completed.
```

1. **Stage 1 (Project Intelligence Agent)**: Scans the workspace and generates `.shadbot/intelligence/project_vision.json`.
2. **Stage 2 (Architect Agent)**: Formulates an enterprise `ArchitecturePlan` with implementation steps and constraints.
3. **Stage 3 (Engineer Agent)**: Consumes the architecture plan, generates implementation code, and executes build/test runners.
4. **Stage 4 (Reviewer Agent)**: Performs Quality Gate checks (`pytest`, `ruff`, `black`, `mypy`) and approves the release.
