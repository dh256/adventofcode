import pytest
from submarine import Submarine

test_data = [('tests/test1.txt',150)]
test_data2 = [('tests/test1.txt',900)]

@pytest.mark.parametrize('filename,result',test_data)
def test_followcourse1(filename,result):
    sub = Submarine(filename)
    sub.follow_course()
    assert(sub.v_pos * sub.h_pos == result)

@pytest.mark.parametrize('filename,result',test_data2)
def test_followcourse2(filename,result):
    sub = Submarine(filename)
    sub.follow_course2()
    assert(sub.v_pos * sub.h_pos == result)