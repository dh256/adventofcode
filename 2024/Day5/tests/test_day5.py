
''' 
David Hanley, December 2024
'''
import pytest
from Day5 import Day5

test_data1=[('tests/test1.txt',143,[3,4,5])]
test_data2=[('tests/test1.txt',[3,4,5],123)]
                  
@pytest.mark.parametrize('file_name,result,invalid_indices',test_data1)
def test_part1(file_name: str,result: int,invalid_indices: list[int]):
    d = Day5(file_name)
    assert(d.part1() == (result,invalid_indices))


@pytest.mark.parametrize('file_name,invalid_indices,result',test_data2)
def test_part2(file_name: str,invalid_indices: list[int], result: int):
    d = Day5(file_name)
    assert(d.part2(invalid_indices) == result)


