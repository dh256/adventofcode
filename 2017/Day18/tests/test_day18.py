from Day18 import Day18
import pytest

test_data =[('tests/test1.txt',4)]
test_data2 =[('tests/test2.txt',3)]

@pytest.mark.parametrize('file_name,result',test_data)
def tests_part1(file_name,result):
    day18 = Day18(file_name)
    assert(day18.part1() == result)
    
@pytest.mark.parametrize('file_name,result',test_data2)
def tests_part1(file_name,result):
    day18 = Day18(file_name)
    assert(day18.part2() == result)