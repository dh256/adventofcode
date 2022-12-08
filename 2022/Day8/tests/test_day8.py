import pytest
from Trees import Trees

test_data=[('tests/test1.txt',21)]
test_data2=[('tests/test1.txt',8)]

@pytest.mark.parametrize('file_name,visible',test_data)
def test_number_visible(file_name,visible):
    trees = Trees(file_name)
    assert(trees.number_visible() == visible)

@pytest.mark.parametrize('file_name,visible',test_data2)
def test_scenic_score(file_name,visible):
    trees = Trees(file_name)
    assert(trees.scenic_score() == visible)

