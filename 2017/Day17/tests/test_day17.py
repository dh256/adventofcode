from Day17 import Day17
import pytest

test_data =[(3,638)]

@pytest.mark.parametrize('steps,result',test_data)
def tests_part1(steps,result):
    day17 = Day17(steps)
    assert(day17.part1() == result)