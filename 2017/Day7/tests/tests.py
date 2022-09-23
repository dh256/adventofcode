from Tower import Tower
import pytest

test_data=[('tests/test1.txt','tknk')]
test_data2=[('tests/test1.txt',60)]

@pytest.mark.parametrize('filename,root_name',test_data)
def test_root(filename,root_name):
    tower = Tower(filename)
    assert(tower.root.id == root_name)

@pytest.mark.parametrize('filename,new_weight',test_data2)
def test_new_weight(filename,new_weight):
    tower = Tower(filename)
    assert(tower.correct_weight_to_balance() == new_weight)


