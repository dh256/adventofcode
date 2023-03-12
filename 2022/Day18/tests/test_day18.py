import pytest
from Cubes import Cubes

test_data=[('tests/test1.txt',10),('tests/test2.txt',64)]

@pytest.mark.parametrize('file_name,surface_area',test_data)
def test_function(file_name: str,surface_area: int):
    cubes = Cubes(file_name)
    assert(cubes.calc_surface_area() == surface_area)