import pytest
from Computer import Computer
from Binary import Binary

test_data = [('test1.txt',165)]
test_data2 = [('test2.txt',208)]
test_data3 = [(1,'0'*35+'1'),(pow(2,35),'1'+'0'*35),(64,'0'*29+'1000000'),(65,'0'*29+'1000001'),(pow(2,35)+65,'1' + '0'*28+'1000001')]

@pytest.mark.parametrize('num,result',test_data3)
def test_binary(num,result):
    bin = Binary(num,36)
    assert f'{bin}' == result
    assert bin.num == num

@pytest.mark.parametrize('file_name,result',test_data)
def test_run(file_name,result):
    computer = Computer(file_name)
    assert computer.run() == result

@pytest.mark.parametrize('file_name,result',test_data2)
def test_run2(file_name,result):
    computer = Computer(file_name)
    assert computer.run2() == result