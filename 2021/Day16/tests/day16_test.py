import pytest
from bits import Bits

test_data = [('tests/test1.txt',16),('tests/test2.txt',12),('tests/test3.txt',23),('tests/test4.txt',31),('tests/test5.txt',6),('tests/test6.txt',9),('tests/test7.txt',14)]
test_data2 = [('tests/test8.txt',3),('tests/test9.txt',54),('tests/test10.txt',7),('tests/test11.txt',9),('tests/test12.txt',1),('tests/test13.txt',0),('tests/test14.txt',0),('tests/test15.txt',1)]

@pytest.mark.parametrize('filename,result',test_data)
def test_version_sum(filename,result):
    bits = Bits(filename)
    assert(bits.version_sum() == result)

@pytest.mark.parametrize('filename,result',test_data2)
def test_evaluate(filename,result):
    bits = Bits(filename)
    assert(bits.evaluate() == result)