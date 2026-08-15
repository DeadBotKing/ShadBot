"""
ShadBot Agent Platform - Pytest Configuration.
Automatically inserts 'src/' into sys.path so all 202 tests pass on Windows/Linux/macOS without needing PYTHONPATH=src or editable installation.
"""

from __future__ import annotations

import sys
from pathlib import Path

src_dir = (Path(__file__).resolve().parent / "src").resolve()
if src_dir.exists() and str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))
