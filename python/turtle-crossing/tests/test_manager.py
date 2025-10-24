import pytest
from manager import Manager

@pytest.fixture
def manager():
    return Manager()

def test_create_car_adds_to_list(manager):
    initial = len(manager.all_cars)
    manager.create_car()
    assert len(manager.all_cars) >= initial

def test_level_up_increases_speed(manager):
    old_speed = manager.car_speed
    manager.level_up()
    assert manager.car_speed > old_speed

def test_reset_clears_all_cars(manager):
    manager.create_car()
    manager.reset()
    assert len(manager.all_cars) == 0
    assert manager.car_speed == 5
