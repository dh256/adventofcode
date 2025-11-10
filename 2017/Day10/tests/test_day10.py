import pytest
from Day10 import Day10

test_data=[('tests/test1.txt',5,12)]
test_data2=[('tests/test1.txt',[65,27,9,1,4,3,40,50,91,7,6,0,2,5,68,22],64)]
test_data3=[('tests/test2.txt','3efbe78a8d82f29979031a4aa0b16a9d'),('tests/test3.txt','63960835bcdc130f0b66d7ff4f6a5a8e')]

@pytest.mark.parametrize('file_name,list_elements,hash',test_data)
def tests_part1(file_name,list_elements,hash):
    day10: Day10 = Day10(file_name)
    assert(day10.part1(list_elements) == hash)
    
@pytest.mark.parametrize('file_name,num_list,result',test_data2)
def tests_list_x_or(file_name,num_list,result):
    day10: Day10 = Day10(file_name)
    assert(day10.x_or_list(num_list) == result)
    
@pytest.mark.parametrize('file_name,result',test_data3)
def tests_part2(file_name,result):
    day10: Day10 = Day10(file_name)
    assert(day10.part2() == result)