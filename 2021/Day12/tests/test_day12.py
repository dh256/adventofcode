import pytest

from cave import Cave

test_data = [('tests/test1.txt',10),('tests/test2.txt',19),('tests/test3.txt',226),('tests/test4.txt',1),('tests/test5.txt',2),('tests/test6.txt',2),('tests/test7.txt',3)]
test_data2 = [('tests/test1.txt',36),('tests/test2.txt',103),('tests/test3.txt',3509)]

@pytest.mark.parametrize('filename,result',test_data)
def test_calc_num_paths(filename,result):
    cave = Cave(filename)
    assert(cave.calc_num_paths() == result)

@pytest.mark.parametrize('filename,result',test_data2)
def test_calc_num_paths2(filename,result):
    cave = Cave(filename)
    assert(cave.calc_num_paths2() == result)