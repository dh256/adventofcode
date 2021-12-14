from polymer import Polymer
import pytest

test_data = [('tests/test1.txt',10,1588),('tests/test1.txt',40,2188189693529)]

@pytest.mark.parametrize('filename,steps,result',test_data)
def test_element_diff2(filename,steps,result):
    poly = Polymer(filename)
    assert(poly.element_difference2(steps) == result)