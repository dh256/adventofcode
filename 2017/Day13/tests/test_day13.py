import pytest
from Day13 import Day13

test_data=[('tests/test1.txt',24)]
test_data2=[('tests/test1.txt',10)]

@pytest.mark.parametrize('file_name,result',test_data)
def tests_part1(file_name,result):
    day13 = Day13(file_name)
    assert(day13.part1() == result)
    
@pytest.mark.parametrize('file_name,result',test_data2)
def tests_part2(file_name,result):
    day13 = Day13(file_name)
    assert(day13.part2() == result)
