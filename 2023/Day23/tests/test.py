from Hike import Hike
import pytest

test_data=[('tests/input.txt',94)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_part1(file_name,result):
    hike = Hike(file_name)
    assert(hike.part1() == result)

    

