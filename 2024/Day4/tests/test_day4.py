
''' 
David Hanley, December 2024
'''
import pytest
from Day4 import Day4

test_data1=[('tests/test1.txt',(18,9))]
                  
@pytest.mark.parametrize('file_name,result',test_data1)
def test_part1(file_name: str,result: tuple[int,int]):
    d = Day4(file_name)
    assert(d.solution() == result)


