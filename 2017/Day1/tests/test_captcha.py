import pytest
from Captcha import Captcha

test_data = [("test1.txt",3),("test2.txt",4),("test3.txt",0),("test4.txt",9)]
test_data2 = [("test5.txt",6),("test6.txt",0),("test7.txt",4),("test8.txt",12),("test9.txt",4)]

@pytest.mark.parametrize('input_file, result',test_data)
def test_sum(input_file, result):
    captcha = Captcha(input_file)
    assert(captcha.sum() == result)

@pytest.mark.parametrize('input_file, result',test_data2)
def test_sum2(input_file, result):
    captcha = Captcha(input_file)
    assert(captcha.sum2() == result)