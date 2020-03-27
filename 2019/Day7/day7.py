from Computer import Computer
from Amplifier import Amplifiers
from SequenceCodes import SequenceCodes

filename = "input.txt"

# PART 1
number_of_amps = 5
sequence_codes=SequenceCodes(0,4,number_of_amps).codes
amps = Amplifiers(filename,number_of_amps,sequence_codes)
max_signal = amps.get_max_thruster_signal()
print(f'Max signal: {max_signal}')

# PART 2
number_of_amps = 5
sequence_codes= SequenceCodes(5,9,number_of_amps).codes
amps = Amplifiers(filename,number_of_amps,sequence_codes)
max_signal = amps.get_max_thruster_signal()
print(f'Max signal: {max_signal}')