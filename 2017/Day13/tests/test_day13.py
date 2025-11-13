import pytest
from Day13 import Day13

test_data=[('tests/test1.txt',24)]


@pytest.mark.parametrize('file_name,result',test_data)
def tests_part1(file_name,result):
    day13 = Day13(file_name)
    assert(day13.part1() == result)
    

