
import pytest
from Day1 import Day1

test_data1=[('tests/input.txt',3,6)]
                  
@pytest.mark.parametrize('file_name,result1, result2',test_data1)
def test_part1and2(file_name: str,result1: int,result2: int):
    d = Day1(file_name)
    assert(d.part1and2() == (result1, result2))


