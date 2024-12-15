
''' 
David Hanley, December 2024
'''
import pytest
from Day14 import Day14

test_data1=[('tests/test1.txt',11,7,12)]
                  
@pytest.mark.parametrize('file_name,width,height,result',test_data1)
def test_part1(file_name: str,width: int,height: int, result: int):
    d = Day14(file_name,width,height)
    assert(d.part1() == result)


