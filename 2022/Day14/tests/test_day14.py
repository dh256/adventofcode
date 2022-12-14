import pytest
from Cave import Cave

test_data=[('tests/test1.txt',24)]
test_data2=[('tests/test1.txt',93)]


@pytest.mark.parametrize('file_name,result',test_data)
def test_function(file_name,result):
    cave = Cave(file_name)
    assert(cave.falling_sand() == result)


@pytest.mark.parametrize('file_name,result',test_data2)
def test_falling_sand2(file_name,result):
    cave = Cave(file_name)
    assert(cave.falling_sand2() == result)