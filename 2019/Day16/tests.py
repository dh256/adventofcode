import pytest
from FFT import FFT

test_data_part1=[
    ("test1.txt",4,"01029498"),
    ("test2.txt",100,"24176176"),
    ("test3.txt",100,"73745418"),
    ("test4.txt",100,"52432133")
]

test_data_part2=[
    ("test5.txt",100,10000,"84462026"),
    ("test6.txt",100,10000,"78725270"),
    ("test7.txt",100,10000,"53553731")
]

@pytest.mark.parametrize("filename,phases,result",test_data_part1)
def test_fft_part1(filename,phases,result):
    fft = FFT(filename)
    assert(fft.run(phases) == result)

@pytest.mark.parametrize("filename,phases,repeat_input,result",test_data_part2)
def test_fft_part2(filename,phases,repeat_input,result):
    fft = FFT(filename)
    assert(fft.run(phases,repeat_input) == result)
