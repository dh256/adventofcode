import pytest
from Sonar import Sonar

test_data1 = [('tests/test1.txt',7)]
test_data2 = [('tests/test1.txt',5)]

@pytest.mark.parametrize('input_file,inc',test_data1)
def test_inc(input_file,inc):
    sonar = Sonar(input_file)
    assert(sonar.increased == inc )

@pytest.mark.parametrize('input_file,inc',test_data2)
def test_inc2(input_file,inc):
    sonar = Sonar(input_file)
    assert(sonar.increased2 == inc)