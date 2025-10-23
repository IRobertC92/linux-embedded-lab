import pytest
from unittest.mock import MagicMock, patch
import sys

@pytest.fixture
def mock_timer():
    """Create a PomodoroTimer instance with a mocked Tk root."""
    from pomodoro_timer import PomodoroTimer
    mock_root = MagicMock()
    timer = PomodoroTimer(
        root=mock_root,
        work_min=0.05,
        short_break_min=0.02,
        long_break_min=0.03,
        sound=False
    )
    mock_root.after = MagicMock()
    mock_root.after_cancel = MagicMock()
    return timer

def test_initial_state(mock_timer):
    """Verify that the timer initializes correctly."""
    assert mock_timer.reps == 0
    assert mock_timer.timer is None
    assert mock_timer.work_min == 0.05

def test_start_timer_increments_reps(mock_timer):
    """Ensure each start_timer() increases reps."""
    prev_reps = mock_timer.reps
    mock_timer._count_down = MagicMock()
    mock_timer._set_title = MagicMock()
    mock_timer.start_timer()
    assert mock_timer.reps == prev_reps + 1

def test_set_title_for_work_session(mock_timer):
    """Safely verify _set_title calls config on label."""
    if hasattr(mock_timer, "label"):
        target_label = mock_timer.label
    elif hasattr(mock_timer, "title_label"):
        target_label = mock_timer.title_label
    else:
        target_label = MagicMock()
        mock_timer.label = target_label

    target_label.config = MagicMock()
    mock_timer._set_title("Work", "#e7305b")
    assert target_label.config.called, "_set_title() did not call config()"

def test_countdown_triggers_next_session(mock_timer):
    """Simulate countdown reaching zero and ensure start_timer is called."""
    mock_timer.start_timer = MagicMock()
    mock_timer.root.after = MagicMock()
    mock_timer._count_down(0)
    mock_timer.start_timer.assert_called_once()

def test_reset_timer_resets_state(mock_timer):
    """Ensure reset_timer cancels timer and resets reps."""
    mock_timer.label = MagicMock()
    mock_timer.check_marks = MagicMock()
    mock_timer.canvas = MagicMock()
    mock_timer.timer = "dummy_id"
    mock_timer.reps = 4

    mock_timer.reset_timer()

    mock_timer.root.after_cancel.assert_called_once_with("dummy_id")
    assert mock_timer.reps == 0

def test_play_sound_windows(monkeypatch):
    """Ensure play_sound() runs without errors on Windows."""
    import pomodoro_timer

    with monkeypatch.context() as m:
        m.setattr(sys, "platform", "win32")
        # Patch winsound import to a dummy module to avoid real sound
        dummy_winsound = MagicMock()
        m.setitem(sys.modules, "winsound", dummy_winsound)
        pomodoro_timer.play_sound()

    # Simply confirm function executed — no exception raised
    assert True

def test_play_sound_non_windows(monkeypatch):
    """Ensure play_sound() runs safely on non-Windows OS."""
    import pomodoro_timer
    with monkeypatch.context() as m:
        m.setattr(sys, "platform", "linux")
        pomodoro_timer.play_sound()
    assert True