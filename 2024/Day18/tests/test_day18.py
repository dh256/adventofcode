
''' 
David Hanley, December 2024
'''
import pytest
from Day18 import Day18,Point

test_data1=[('tests/test1.txt',7,7,12,22)]
test_data2=[('tests/test1.txt',7,7,Point(6,1))]
                  
@pytest.mark.parametrize('file_name,grid_width,grid_height,num_bytes,result',test_data1)
def test_part1(file_name: str,grid_width:int,grid_height:int,num_bytes:int,result: int):
    d = Day18(file_name,grid_width,grid_height)
    assert(d.part1(num_bytes) == result)

@pytest.mark.parametrize('file_name,grid_width,grid_height,result',test_data2)
def test_part2(file_name,grid_width:int,grid_height:int,result: Point):
    d = Day18(file_name,grid_width,grid_height)
    assert(d.part2() == result)

