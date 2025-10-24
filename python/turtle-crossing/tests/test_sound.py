import pytest
from sound import SoundManager
import os

@pytest.fixture
def sm():
    return SoundManager()

def test_init_creates_empty_dict(sm):
    assert isinstance(sm.sounds, dict)
    assert len(sm.sounds) == 0

def test_load_nonexistent_file_raises(sm, tmp_path):
    with pytest.raises(FileNotFoundError):
        sm.load_sound("missing", tmp_path / "nofile.wav")

def test_load_and_play_mock(sm, tmp_path, monkeypatch):
    # create a dummy wav file
    dummy_file = tmp_path / "dummy.wav"
    dummy_file.write_bytes(b"RIFF....WAVE")  # minimal WAV header

    sm.load_sound("dummy", str(dummy_file))
    
    # Mock the play method to just record call
    played = []
    monkeypatch.setattr(sm.sounds["dummy"], "play", lambda loops=0: played.append(True))
    
    sm.play("dummy")
    assert played