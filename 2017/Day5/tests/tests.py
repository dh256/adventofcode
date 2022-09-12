import pytest
from CPU import CPU 

test_data=[('tests/test1.txt',5)]
test_data2=[('tests/test1.txt',10)]

@pytest.mark.parametrize('filename,steps',test_data)
def test_process(filename,steps):
    cpu = CPU(filename)
    assert(cpu.process() == steps)

@pytest.mark.parametrize('filename,steps',test_data2)
def test_process2(filename,steps):
    cpu = CPU(filename)
    assert(cpu.process2() == steps)
