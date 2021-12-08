import pytest
from display import Display 

test_data = [('tests/test1.txt',0),('tests/test2.txt',26)]
test_data2 = [('tests/test1.txt',5353),('tests/test2.txt',61229)]

@pytest.mark.parametrize('filename,result',test_data)
def test_digits_appear(filename,result):
    display = Display(filename)
    assert(display.digits_appear() == result)

@pytest.mark.parametrize('filename,result',test_data2)
def test_output_sum(filename,result):
    display = Display(filename)
    assert(display.output_sum() == result)