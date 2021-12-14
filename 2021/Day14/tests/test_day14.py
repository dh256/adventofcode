from polymer import Polymer
import pytest

test_data1 = [('tests/test1.txt',1,'NCNBCHB'),('tests/test1.txt',4,'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')]
test_data2 = [('tests/test1.txt',10,1588)]

@pytest.mark.parametrize('filename,steps,result',test_data1)
def test_grow_polymer(filename,steps,result):
    poly = Polymer(filename)
    poly.grow_polymer(steps)
    assert(poly.polymer == result)

@pytest.mark.parametrize('filename,steps,result',test_data2)
def test_element_diff(filename,steps,result):
    poly = Polymer(filename)
    assert(poly.element_difference(steps) == result)