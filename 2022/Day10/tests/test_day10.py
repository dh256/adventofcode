import pytest
from CathodeRayTube import CPU

test_data=[('tests/test1.txt',[20,60,100,140,180,220],13140)]

@pytest.mark.parametrize('file_name,cycles,result',test_data)
def test_function(file_name,cycles,result):
    cpu = CPU(file_name)
    cpu.run_instructions()
    assert(cpu.sum_signal_strengths(cycles) == result)