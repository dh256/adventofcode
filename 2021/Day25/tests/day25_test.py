import pytest
from SeaCucumbers import SeaCucumbers

test_data = [("tests/test1.txt",58)]

@pytest.mark.parametrize('input_file,result',test_data)
def test_func(input_file,result):
    cucumbers = SeaCucumbers(input_file)
    assert(cucumbers.stepsNoMove() == result)

