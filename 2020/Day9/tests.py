from Port import Port
import pytest

test_data = [('test1.txt',25,65),('test2.txt',5,127)]
test_data2 = [('test2.txt',5,62)]

@pytest.mark.parametrize("file_name,preamble_len,result",test_data)
def test_first_number_not_compliant(file_name,preamble_len,result):
    port = Port(file_name,preamble_len)
    assert port.first_number_not_compliant() == result

@pytest.mark.parametrize("file_name,preamble_len,result",test_data2)
def test_encryption_weakness(file_name,preamble_len,result):
    port = Port(file_name,preamble_len)
    assert port.encryption_weakness() == result
