import pytest
from File import File

test_data = [("test1.txt",6),
            ("test2.txt",7),
            ("test3.txt",11),
            ("test4.txt",6),
            ("test5.txt",18)]

test_data2 = [("test6.txt",9),
            ("test7.txt",20),
            ("test8.txt",241920),
            ("test9.txt",445)]

@pytest.mark.parametrize("file,decompressed_length",test_data)
def test_decompress(file,decompressed_length):
    file = File(file)
    assert(len(file.decompress()) == decompressed_length)

@pytest.mark.parametrize("file,decompressed_length",test_data2)
def test_decompress2(file,decompressed_length):
    file = File(file)
    assert(file.decompress2() == decompressed_length)