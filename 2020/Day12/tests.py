import pytest
from Ship import Ship, ShipMoveMode

test_data = [('test1.txt',ShipMoveMode.SHIP,25),('test1.txt',ShipMoveMode.WAYPOINT,286)]

@pytest.mark.parametrize('file_name,mode,distance',test_data)
def test_navigate(file_name,mode,distance):
    ship = Ship(file_name)
    ship.reset()
    assert ship.navigate(mode) == distance