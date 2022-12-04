import pytest
from Space import Space

test_data=[('tests/test1.txt',2)]
test_data2=[('tests/test1.txt',4)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_pairs_contained_within(file_name,result):
    space = Space(file_name)
    assert(space.pairs_contained_within() == result)

@pytest.mark.parametrize('file_name,result',test_data2)
def test_pairs_overlap_at_all(file_name,result):
    space = Space(file_name)
    assert(space.pairs_overlap_at_all() == result)