import pytest
from CPU import CPU

test_data=[('tests/test1.txt',1,10)]

@pytest.mark.parametrize('filename,highest_at_end,highest_ever',test_data)
def test_process(filename,highest_at_end,highest_ever):
    cpu = CPU(filename)
    result = cpu.process()
    assert(result[0] == highest_at_end)
    assert(result[1] == highest_ever)