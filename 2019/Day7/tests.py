import pytest
from Amplifier import Amplifiers

test_data_part1 = [
    ("test1.txt",5,[(4,3,2,1,0)],43210),
    ("test2.txt",5,[(0,1,2,3,4)],54321),
    ("test3.txt",5,[(1,0,4,3,2)],65210)
]

test_data_part2 = [
    ("test4.txt",5,[(9,8,7,6,5)],139629729),
    ("test5.txt",5,[(9,7,8,5,6)],18216)
]

@pytest.mark.parametrize("filename,amps,phase_setting,thrust",test_data_part1)
def test_max_signal_thrust_part1(filename,amps,phase_setting,thrust):
    amps=Amplifiers(filename,amps,phase_setting)
    assert(amps.get_max_thruster_signal() == thrust)

@pytest.mark.parametrize("filename,amps,phase_setting,thrust",test_data_part2)
def test_max_signal_thrust_part2(filename,amps,phase_setting,thrust):
    amps=Amplifiers(filename,amps,phase_setting)
    assert(amps.get_max_thruster_signal() == thrust)
