SHADBOT MLFIX2 PATCH — 2026-08-13
=================================

This archive is a PATCH, not a full project.

It overwrites the files that still produce:

    [AGENT ERROR] Experiment command required.

WHY THE LAST ZIP DID NOT FIX IT
-------------------------------
ShadBot-fixed.zip already changed experiment_executor_adapter.py so it
no longer raises that error. You are still seeing the error, which means
Windows is executing an OLD adapter (old folder, old .venv, or
site-packages). This patch fixes the failure in THREE layers:

1. ml_scientist_agent.py always sends a command payload
2. experiment_executor_adapter.py never raises "Experiment command required."
3. tool_executor.py retries once if a leftover old adapter still raises

INSTALL (do this exactly)
-------------------------
1. Close every PowerShell / VS Code terminal that is inside
   C:\Users\DeadBotKing\Desktop\ShadBot-fixed\ShadBot

2. Extract this zip. You will get:

      mlfix2\ShadBot\run_agent.py
      mlfix2\ShadBot\src\...
      mlfix2\ShadBot\READ_ME_FIRST_MLFIX.txt

3. Copy the CONTENTS of mlfix2\ShadBot\ on top of your existing project,
   overwriting files:

      from:  <extract>\mlfix2\ShadBot\*
      to:    C:\Users\DeadBotKing\Desktop\ShadBot-fixed\ShadBot\

   In Explorer: open mlfix2\ShadBot, Ctrl+A, copy, paste into
   ShadBot-fixed\ShadBot, choose Replace.

4. Delete leftover bytecode so Python cannot load the old adapter:

      Remove-Item -Recurse -Force .\src\agentplatform\infrastructure\tools\__pycache__ -ErrorAction SilentlyContinue
      Remove-Item -Recurse -Force .\src\agentplatform\infrastructure\agents\__pycache__ -ErrorAction SilentlyContinue
      Remove-Item -Recurse -Force .\src\agentplatform\application\tooling\__pycache__ -ErrorAction SilentlyContinue

5. Run from the project folder with the same venv:

      python run_agent.py

YOU MUST SEE THIS FIRST
-----------------------
    ===========================================================================
    SHADBOT BUILD: 2026-08-13-mlfix2
    EXPERIMENT ADAPTER FILE: ...\ShadBot\src\agentplatform\infrastructure\tools\experiment_executor_adapter.py
    EXPERIMENT ADAPTER BUILD: 2026-08-13-mlfix2
    ===========================================================================

If that banner is missing, you launched an old run_agent.py.
If EXPERIMENT ADAPTER FILE points at site-packages or another Desktop
folder, Python is importing the old package. Then create a NEW venv:

      python -m venv .venv-mlfix2
      .\.venv-mlfix2\Scripts\Activate.ps1
      pip install -r requirements.txt
      python run_agent.py

When ML_SCIENTIST starts you must also see:

    [ML_SCIENTIST] build=2026-08-13-mlfix2 evaluating experiments for ...

FILES IN THIS PATCH
-------------------
- run_agent.py
- src/agentplatform/infrastructure/agents/ml_scientist_agent.py
- src/agentplatform/infrastructure/tools/experiment_executor_adapter.py
- src/agentplatform/application/tooling/tool_executor.py
- src/agentplatform/infrastructure/tools/test_runner.py
- src/agentplatform/infrastructure/registration/tool_registration.py
- tests/agentplatform_tests/agents/test_ml_scientist_agent.py
- SHADBOT_BUILD.txt
