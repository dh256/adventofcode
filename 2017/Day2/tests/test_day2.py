import pytest
from Spreadsheet import Spreadsheet

test_data = [("test1.txt",18)]
test_data2 = [("test2.txt",9)]

@pytest.mark.parametrize('input_file,result',test_data)
def test_checksum(input_file, result):
    sheet = Spreadsheet(input_file)
    assert(sheet.check_sum == result)

@pytest.mark.parametrize('input_file,result',test_data2)
def test_checksum2(input_file, result):
    sheet = Spreadsheet(input_file)
    assert(sheet.check_sum2 == result)