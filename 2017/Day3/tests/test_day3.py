import pytest
from Day3 import Day3

test_data=[(1,1,0),(1,9,2),(1,12,3),(1,13,4),(1,17,4),(1,23,2),(1,25,4),(1,1024,31),(2,0,1),(2,1,2),(2,3,4),(2,4,5),(2,5,10),(2,10,11),(2,11,23),(2,23,25),(2,25,26),(2,26,54),(2,54,57),(2,57,59),(2,747,806)]

@pytest.mark.parametrize('part,number,result',test_data)
def tests_part1(part:int, number: int, result: int):
    day3: Day3 = Day3(number)
    assert(day3.solution(part) == result)
    