import pytest
from Memory import Memory

test_data=[('tests/test1.txt',1,5),('tests/test1.txt',2,9)]

@pytest.mark.parametrize('filename,rounds,result',test_data)
def test_function(filename,rounds,result):
    memory = Memory(filename)
    assert(memory.restribute(rounds) == result)

