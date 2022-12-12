import pytest
from HillClimbing import Hills

test_data=[('tests/test1.txt',31)]
test_data2=[('tests/test1.txt',29)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_find_shortest_path(file_name,result):
    hills = Hills(file_name)
    assert(hills.find_shortest_path() == result)

@pytest.mark.parametrize('file_name,result',test_data2)
def test_shortest_path2(file_name,result):
    hills = Hills(file_name)
    assert(hills.find_shortest_path2() == result)


