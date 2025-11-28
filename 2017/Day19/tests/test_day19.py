import pytest
from Day19 import Day19

test_data = [('tests/test1.txt','ABCDEF',38)]

@pytest.mark.parametrize('file_name,result1,result2',test_data)
def test_part1(file_name: str, result1: str, result2: int):
    day19 = Day19(file_name)
    result = day19.part1and2()
    assert(result1 == result[0])
    assert(result2 == result[1])