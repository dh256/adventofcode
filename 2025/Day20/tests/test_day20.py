
import pytest
from Day20 import Day20

test_data1=[('2025/Day20/tests/input.txt',0)]
#test_data2=[('2025/Day20/tests/input.txt',0)]
                  
@pytest.mark.parametrize('file_name,result',test_data1)
def test_part1(file_name,result):
    d = Day20(file_name)
    assert(d.part1() == result)

'''
@pytest.mark.parametrize('file_name,result',test_data2)
def test_part2(file_name,result):
    d = Day20(file_name)
    assert(d.part2() == result)
'''
