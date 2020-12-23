import pytest
from Ship import Ship

test_data = [('test1.txt',25)]

@pytest.mark.parametrize('file_name,distance',test_data)
def test_navigate(file_name,distance):
    ship = Ship(file_name)
    assert ship.navigate() == distance
