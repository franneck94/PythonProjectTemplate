import sys
from typing import Any
from typing import Dict

import pytest


@pytest.fixture
def capture_stdout(monkeypatch: pytest.MonkeyPatch) -> Dict[str, Any]:
    buffer: Dict[str, Any] = {"stdout": "", "writecalls": 0}

    def fake_writer(s):
        buffer["stdout"] += s
        buffer["writecalls"] += 1

    monkeypatch.setattr(sys.stdout, "write", fake_writer)
    return buffer
