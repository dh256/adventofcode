import pytest
from Eris import Eris

test_data = [
    ('test.txt',1205552,2129920)
]

@pytest.mark.parametrize("filename,hash,biodiversity",test_data)
def test_biodiversity(filename,hash,biodiversity):
    eris = Eris(filename)
    assert(eris.__hash__() == hash)
    assert(eris.biodiversity() == biodiversity)