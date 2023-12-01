
import pytest
from WeatherMachine import WeatherMachine

test_data=[('tests/input.txt',1,142)]
test_data2=[('tests/input2.txt',2,281)]

@pytest.mark.parametrize('file_name,part,result',test_data)
def test_sum_calibration_values(file_name,part,result):
    wm = WeatherMachine(file_name)
    assert(wm.sum_calibration_values(part) == result)
