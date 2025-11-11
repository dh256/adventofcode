import pytest
from Day12 import Day12

test_data=[('tests/test1.txt',6)]
test_data2=[('tests/test1.txt',2)]

@pytest.mark.parametrize('file_name,result',test_data)
def tests_part1(file_name,result):
    day12 = Day12(file_name)
    assert(day12.part1() == result)
    
@pytest.mark.parametrize('file_name,result',test_data2)
def tests_part2(file_name,result):
    day12 = Day12(file_name)
    assert(day12.part2() == result)
