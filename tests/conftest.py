"""
Conftest module.
"""

import sys
from typing import Any
from typing import Dict

import pytest


@pytest.fixture
def capture_stdout(
    monkeypatch: pytest.MonkeyPatch,
) -> Dict[str, Any]:
    """Capture stdout."""
    buffer: Dict[str, Any] = {"stdout": "", "writecalls": 0}

    def fake_writer(stdout: str) -> None:
        buffer["stdout"] += stdout
        buffer["writecalls"] += 1

    monkeypatch.setattr(sys.stdout, "write", fake_writer)
    return buffer
