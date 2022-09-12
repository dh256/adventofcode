import pytest
from Passphrase import Passphrase

test_data=[('tests/test1.txt',2)]
test_data2=[('tests/test2.txt',3)]

@pytest.mark.parametrize('filename,count',test_data)
def test_valid_phrases(filename,count):
    pass_phrases = Passphrase(filename)
    assert(pass_phrases.valid_phrases() == count)

@pytest.mark.parametrize('filename,count',test_data2)
def test_valid_phrases2(filename,count):
    pass_phrases = Passphrase(filename)
    assert(pass_phrases.valid_phrases2() == count)