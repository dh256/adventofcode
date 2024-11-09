import pytest
from Day8 import Day8

test_data=[('tests/test1.txt',12,19)]

@pytest.mark.parametrize('file_name,part1,part2',test_data)
def test_calculate(file_name:str,part1:int,part2:int):
    day8 = Day8(file_name)
    assert(day8.calculate() == (part1,part2))