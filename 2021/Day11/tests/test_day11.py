from octopus import Octopus
import pytest

test_data =[('tests/test2.txt',1,9),('tests/test1.txt',1,0),('tests/test1.txt',2,35),('tests/test1.txt',10,204),('tests/test1.txt',100,1656)]
test_data2 = [('tests/test1.txt',195)]

@pytest.mark.parametrize('filename,steps,result',test_data)
def test_calc_flashes(filename,steps,result):
    octopus = Octopus(filename)
    assert(octopus.calc_flashes(steps) == result)

@pytest.mark.parametrize('filename,result',test_data2)
def test_calc_all_flash(filename,result):
    octopus = Octopus(filename)
    assert(octopus.calc_all_flash() == result)
