import pytest
from Adapters import Adapters

test_data1 = [('test1.txt',22),('test2.txt',52)]
test_data2 = [('test1.txt',35),('test2.txt',220)]
test_data3 = [('test1.txt',8),('test2.txt',19208)]

@pytest.mark.parametrize("file_name,built_in",test_data1)
def test_built_in(file_name,built_in):
    adapters=Adapters(file_name)
    assert adapters.built_in == built_in

@pytest.mark.parametrize("file_name,answer",test_data2)
def test_part1(file_name,answer):
    adapters=Adapters(file_name)
    assert adapters.part1() == answer

@pytest.mark.parametrize("file_name,answer",test_data3)
def test_part2(file_name,answer):
    adapters=Adapters(file_name)
    assert adapters.part2() == answer