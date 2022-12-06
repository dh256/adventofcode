import pytest
from Device import Device

test_data=[ ('tests/test1.txt',4,7),
            ('tests/test2.txt',4,5),
            ('tests/test3.txt',4,6),
            ('tests/test4.txt',4,10),
            ('tests/test5.txt',4,11),
            ('tests/test1.txt',14,19),
            ('tests/test2.txt',14,23),
            ('tests/test3.txt',14,23),
            ('tests/test4.txt',14,29),
            ('tests/test5.txt',14,26)]



@pytest.mark.parametrize('file_name,chars,result',test_data)
def test_function(file_name,chars,result):
    device = Device(file_name)
    assert(device.first_marker(chars) == result)