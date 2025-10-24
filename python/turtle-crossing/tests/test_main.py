import importlib
import pytest
import sys
from unittest.mock import MagicMock

@pytest.mark.skip(reason="main.py infinite loop, only test init")
def test_main_import(monkeypatch):
    # Mock turtle screen to prevent opening a window
    sys.modules['turtle'].Screen = MagicMock()
    sys.modules['turtle'].Turtle = MagicMock()
    
    # Mock SoundManager to prevent actual audio
    from sound import SoundManager
    monkeypatch.setattr('sound.SoundManager', lambda: MagicMock())

    # Import main
    importlib.import_module("main")