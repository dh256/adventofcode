import pytest

from Cubes import Cubes, Cubes2

test_data = [('test1.txt',1,11),('test1.txt',2,21),('test1.txt',6,112)]
test_data2 = [('test1.txt',1,29),('test1.txt',6,848)]

# Part 1
@pytest.mark.parametrize('file_name,cycles,result',test_data)
def test_simulate_cycles(file_name, cycles, result):
    cubes = Cubes(file_name)
    assert cubes.cycle(cycles) == result

# Part 2
@pytest.mark.parametrize('file_name,cycles,result',test_data2)
def test_simulate_cycles2(file_name, cycles, result):
    cubes = Cubes2(file_name)
    assert cubes.cycle(cycles) == result