'''
David Hanley, November 2024
'''
import pytest
from Day10 import Day10

test_data=[('1',1,2),('111221',1,6)]

@pytest.mark.parametrize('digits,iterations,output_length', test_data)
def test_day_10(digits: str,iterations: int,output_length: int):
    day10 = Day10(digits)
    assert(day10.part1(iterations) == output_length)
    #assert(day10.part2() == result_p2)