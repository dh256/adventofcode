'''
David Hanley, November 2024
'''
import pytest
from Day17 import Day17

test_data1=[('tests/test1.txt',25,4,3)]
                  
@pytest.mark.parametrize('file_name,qty,result_p1,result_p2',test_data1)
def test_part1(file_name: str,qty:int,result_p1: int,result_p2: int):
    d = Day17(file_name,qty)
    assert(d.solution() == (result_p1,result_p2))

