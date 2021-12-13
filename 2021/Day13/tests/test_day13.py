import pytest
from paper import Paper

test_data = [('tests/test1.txt','17')]

@pytest.mark.parametrize('filename,result',test_data)
def test_do_folds(filename,result):
    paper = Paper(filename)
    assert(paper.do_folds() == result)