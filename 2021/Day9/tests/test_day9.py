import pytest
from cave import Cave

test_data = [('tests/test1.txt',15)]
test_data2 = [('tests/test1.txt',3,1134)]

@pytest.mark.parametrize('filename,result',test_data)
def test_find_risk_level(filename, result):
    cave = Cave(filename)
    assert(cave.find_risk_level() == result)

@pytest.mark.parametrize('filename,number,result',test_data2)
def test_find_largest_basins(filename, number, result):
    cave = Cave(filename)
    assert(cave.find_largest_basins(number) == result)