
import pytest
from Network import Network

test_data=[('tests/input1.txt',2),('tests/input2.txt',6)]
test_data2=[('tests/input3.txt',6)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_steps(file_name,result):
    network = Network(file_name)
    assert(network.steps() == result)

@pytest.mark.parametrize('file_name,result',test_data)
def test_steps2(file_name,result):
    network = Network(file_name)
    assert(network.steps2() == result)

