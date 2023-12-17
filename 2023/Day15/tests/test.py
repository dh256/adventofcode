from Hash import Hash
import pytest

test_data=[('tests/input.txt',1320)]
test_data2=[('tests/input.txt',145)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_part1(file_name,result):
    hash = Hash(file_name)
    assert(hash.part1() == result)

@pytest.mark.parametrize('file_name,result',test_data2)
def test_part2(file_name,result):
    hash = Hash(file_name)
    assert(hash.part2() == result)

