import pytest
from Day15 import Day15

test_data=[65,8921,588]
test_data2=[65,8921,309]

@pytest.mark.parametrize('genA,genB,result',test_data)
def tests_part1(genA,genB,result):
    day15 = Day15(genA,genB)
    assert(day15.part1() == result)
    
@pytest.mark.parametrize('genA,genB,result',test_data2)
def tests_part1(genA,genB,result):
    day15 = Day15(genA,genB)
    assert(day15.part2() == result)
    