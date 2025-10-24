import pytest
from score import Score

@pytest.fixture
def score():
    return Score()

def test_initial_level_is_one(score):
    assert score.level == 1

def test_increase_level(score):
    score.increase_level()
    assert score.level == 2

def test_reset(score):
    score.increase_level()
    score.reset()
    assert score.level == 1

def test_game_over_display(score):
    # just call, no crash expected
    score.game_over()

def test_show_message(score):
    score.show_message("PAUSED")