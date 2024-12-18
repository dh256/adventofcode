
''' 
David Hanley, December 2024
'''
import pytest
from Day17 import Day17

test_data1=[('tests/test1.txt','4,6,3,5,6,3,5,2,1,0')]
# test_data2=[('tests/test1.txt',0)]
                  
@pytest.mark.parametrize('file_name,result',test_data1)
def test_part1(file_name: str,result: str):
    d = Day17(file_name)
    assert(d.part1() == result)

'''
@pytest.mark.parametrize('file_name,result',test_data2)
def test_part2(file_name,result):
    d = Day17(file_name)
    assert(d.part2() == result)
'''

