from Lagoon import Lagoon
import pytest

test_data=[('tests/input.txt',62)]
test_data2=[('tests/input.txt',952408144115)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_part1(file_name,result):
    lagoon = Lagoon(file_name)
    assert(lagoon.part1() == result)

@pytest.mark.parametrize('file_name,result',test_data2)
def test_part2(file_name,result):
    lagoon = Lagoon(file_name)
    assert(lagoon.part2() == result)

