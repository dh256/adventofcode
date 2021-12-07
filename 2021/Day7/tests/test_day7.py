import pytest
from crabs import Crabs

test_data = [('tests/test1.txt',2,37)]
test_data2 = [('tests/test1.txt',5,168)]

@pytest.mark.parametrize('filename,pos,fuel_used',test_data)
def test_align(filename,pos,fuel_used):
    crabs = Crabs(filename)
    result = crabs.align()
    assert(result[0] == pos and result[1] == fuel_used)

@pytest.mark.parametrize('filename,pos,fuel_used',test_data2)
def test_align2(filename,pos,fuel_used):
    crabs = Crabs(filename)
    result = crabs.align2()
    assert(result[0] == pos and result[1] == fuel_used)