
import pytest
from Network import Network

test_data=[('tests/input1.txt',2),('tests/input2.txt',6)]
test_data2=[('tests/input3.txt',6)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_part_one(file_name,result):
    network = Network(file_name)
    assert(network.part_one() == result)

@pytest.mark.parametrize('file_name,result',test_data2)
def test_part_two(file_name,result):
    network = Network(file_name)
    assert(network.part_two() == result)

