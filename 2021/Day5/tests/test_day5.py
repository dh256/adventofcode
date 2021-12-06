import pytest
from vents import Vents

test_data = [('tests/test1.txt',5)]
test_data2 = [('tests/test1.txt',12)]

@pytest.mark.parametrize('filename,result', test_data)
def test_day5_part1(filename,result):
    vents = Vents(filename,1)
    assert(vents.dangerous_areas == result)

@pytest.mark.parametrize('filename,result', test_data2)
def test_day5_part2(filename,result):
    vents = Vents(filename,2)
    assert(vents.dangerous_areas == result)