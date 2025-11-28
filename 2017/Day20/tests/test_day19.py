import pytest
from Day20 import Day20

test_data = [('tests/test1.txt',0)]
test_data2 = [('tests/test2.txt',1)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_part1(file_name: str, result: int):
    day20 = Day20(file_name)
    assert(day20.part1() == result)
    
@pytest.mark.parametrize('file_name,result',test_data2)
def test_part2(file_name: str, result: int):
    day20 = Day20(file_name)
    assert(day20.part2() == result)
    