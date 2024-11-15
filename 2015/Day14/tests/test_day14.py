'''
David Hanley, November 2024
'''
import pytest
from Day14 import Day14

test_data1=[('tests/test1.txt',1,16),
            ('tests/test1.txt',10,160),
            ('tests/test1.txt',11,176),
            ('tests/test1.txt',1000,1120)]

test_data2=[('tests/test1.txt',1,1),
            ('tests/test1.txt',140,139),
            ('tests/test1.txt',1000,689)]
                  
@pytest.mark.parametrize('file_name,interval,result',test_data1)
def test_part1(file_name:str,interval:int,result:int):
    d = Day14(file_name)
    assert(d.part1(interval) == result)

@pytest.mark.parametrize('file_name,interval,result',test_data2)
def test_part2(file_name:str,interval:int,result:int):
    d = Day14(file_name)
    assert(d.part2(interval) == result)
