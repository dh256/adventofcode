from Hike import Hike
import pytest

test_data=[('tests/input.txt',94)]
test_data2=[('tests/input.txt',154)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_part1(file_name,result):
    hike = Hike(file_name)
    assert(hike.part1_alt() == result)

@pytest.mark.parametrize('file_name,result',test_data2)
def test_part2(file_name,result):
    hike = Hike(file_name)
    assert(hike.part2_alt() == result)

    

