
''' 
David Hanley, December 2024
'''
import pytest
from Day6 import Day6

test_data=[('tests/test1.txt',41,6)]
                  
@pytest.mark.parametrize('file_name,result_p1,result_p2',test_data)
def test_solutions(file_name: str,result_p1: int,result_p2: int):
    d = Day6(file_name)
    positions = d.part1()
    assert(len(positions) == result_p1)
    assert(d.part2(positions) == result_p2)


