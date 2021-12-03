from enum import Enum

class GasType(Enum):
    O2=0
    CO2=1 
 
class Submarine:

    def __init__(self,filename):
        with open(filename,'r') as input_file:
            self.diagnostic_codes = [line.strip('\n') for line in input_file]
            self.diagnostic_code_len = len(self.diagnostic_codes[0])   # assume all the same length

    def calculate_gamma_epsilon(self):
        gamma = ''
        epsilon = ''
        for index in range(0,self.diagnostic_code_len):
            zero_count = 0
            one_count = 0
            for diagnostic_code in self.diagnostic_codes:
                if diagnostic_code[index] == '0':
                    zero_count += 1
                else:
                    one_count +=1 

            # work out gamma, epsilon
            if zero_count > one_count:
                gamma += '0'
                epsilon += '1'
            else:
                gamma += '1'
                epsilon += '0'

        return (int(gamma,2),int(epsilon,2))


    def calculate_gas_rating(self,gas_type,codes_remaining=None,bit_position=0):
        if codes_remaining is None:
            codes_remaining = self.diagnostic_codes

        # calculate most common int
        zero_count = 0
        one_count = 0
        for code in codes_remaining:
            if code[bit_position] == '0':
                zero_count += 1
            else:
                one_count +=1 

        # calculate which bit value to keep
        if gas_type == GasType.O2:
            if one_count >= zero_count:
                keep = '1'
            else:
                keep = '0'
        else:
            if zero_count <= one_count:
                keep = '0'
            else:
                keep = '1'

        # filter out codes whose bit at current position don't match keep bit
        codes_remaining = list(filter(lambda x : x[bit_position] == keep, codes_remaining))

        # recurse
        if len(codes_remaining) > 1:
            return self.calculate_gas_rating(gas_type,codes_remaining,bit_position+1)
        else:
            return int(codes_remaining[0],2)

    @property
    def power_consumption(self):
        gamma_epsilon = self.calculate_gamma_epsilon()
        return gamma_epsilon[0] * gamma_epsilon[1]

    @property 
    def life_support_rating(self):
        return self.calculate_gas_rating(GasType.O2) * self.calculate_gas_rating(GasType.CO2)