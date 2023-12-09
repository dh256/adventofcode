from Oasis import Oasis
import pytest

test_data=[('tests/input.txt',1,114),('tests/input.txt',2,2)]

@pytest.mark.parametrize('file_name, part, result',test_data)
def test_sum_of_extrapolated(file_name, part, result):
    oasis = Oasis(file_name)
    assert(oasis.sum_of_extrapolated(part) == result)


