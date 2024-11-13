'''
David Hanley, November 2024
'''
import pytest
from Day9 import Day9

test_data=[('tests/test1.txt',605,982)]

@pytest.mark.parametrize('file_name,result_p1, result_p2',test_data)
def test_day_9(file_name:str,result_p1:int,result_p2:int):
    day9 = Day9(file_name)
    assert(day9.part1() == result_p1)
    assert(day9.part2() == result_p2)