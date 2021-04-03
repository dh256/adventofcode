import pytest
from Homework import Homework

test_data = [('test1.txt',71),('test6.txt',51),('test2.txt',26),('test3.txt',437),('test4.txt',12240),('test5.txt',13632)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_sum_of_lines(file_name,result):
    homework = Homework(file_name)
    assert homework.sum_of_lines() == result
