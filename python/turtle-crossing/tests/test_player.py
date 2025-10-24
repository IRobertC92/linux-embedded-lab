import pytest
from player import Player

@pytest.fixture
def player():
    return Player()

def test_initial_position(player):
    assert round(player.xcor()) == 0
    assert round(player.ycor()) == -280

def test_go_up_increases_y(player):
    y_before = player.ycor()
    player.go_up()
    assert player.ycor() > y_before

def test_reset_to_start(player):
    player.go_up()
    player.go_to_start()
    assert round(player.ycor()) == -280

def test_is_at_finish_line_true(player):
    player.sety(300)
    assert player.is_at_finish_line()