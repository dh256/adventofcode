
import pytest
from Race import Race

test_data=[('tests/input.txt',288)]
test_data2=[('tests/input.txt',71503)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_part1(file_name,result):
    race = Race(file_name)
    assert(race.part1() == result)

@pytest.mark.parametrize('file_name,result',test_data2)
def test_part2(file_name,result):
    race = Race(file_name)
    assert(race.part2() == result)

