import pytest
from Day8 import Day8

test_data=[('tests/test1.txt',12)]

@pytest.mark.parametrize('file_name,value',test_data)
def test_part1(file_name:str,value:int):
    day8 = Day8(file_name)
    assert(day8.part1() == value)