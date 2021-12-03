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

    def calculate_o2_rating(self,codes_remaining=None,bit_position=0):
        if codes_remaining is None:
            codes_remaining = self.diagnostic_codes

        # calculate most common int
        zero_count = 0
        one_count = 0
        keep = '1'
        keep_codes = []
        for code in codes_remaining:
            if code[bit_position] == '0':
                zero_count += 1
            else:
                one_count +=1 

        if zero_count > one_count:
            keep = '0'

        for code in codes_remaining:
            if code[bit_position] == keep:
                keep_codes.append(code)

        # recurse
        if len(keep_codes) > 1:
            self.calculate_o2_rating(keep_codes,bit_position+1)
        else:
            self.o2_rating = int(keep_codes[0],2)
            return

    def calculate_co2_rating(self,codes_remaining=None,bit_position=0):
        if codes_remaining is None:
            codes_remaining = self.diagnostic_codes

        # calculate most common int
        zero_count = 0
        one_count = 0
        keep = '0'
        keep_codes = []
        for code in codes_remaining:
            if code[bit_position] == '0':
                zero_count += 1
            else:
                one_count +=1 

        if one_count < zero_count:
            keep = '1'

        for code in codes_remaining:
            if code[bit_position] == keep:
                keep_codes.append(code)

        # recurse
        if len(keep_codes) > 1:
            self.calculate_co2_rating(keep_codes,bit_position+1)
        else:
            self.co2_rating = int(keep_codes[0],2)
            return

    @property
    def power_consumption(self):
        gamma_epsilon = self.calculate_gamma_epsilon()
        return gamma_epsilon[0] * gamma_epsilon[1]

    @property 
    def life_support_rating(self):
        self.calculate_o2_rating()
        self.calculate_co2_rating()
        return self.o2_rating * self.co2_rating