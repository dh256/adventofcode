
''' 
David Hanley, December 2024
'''
import pytest
from Day25 import Day25

test_data1=[('tests/test1.txt',3)]
                 
@pytest.mark.parametrize('file_name,result',test_data1)
def test_part1(file_name: str,result: int):
    d = Day25(file_name)
    assert(d.part1() == result)



