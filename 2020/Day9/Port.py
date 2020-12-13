import itertools

class Port():

    def __init__(self, file_name, preamble_length):
        self._preamble_length = preamble_length
        with open(file_name,'r') as port_data:
            self._port_numbers = [int(line.strip('\n')) for line in port_data]

    def first_number_not_compliant(self):
        for curr_index in range(self._preamble_length, len(self._port_numbers)):
            # work out all possible 2 number combos from previous self._preamble_length numbers
            # determine whether the sum of any of these add up to number at curr_index
            # if not, return number
            pairs = itertools.permutations(self._port_numbers[curr_index - self._preamble_length:curr_index],2)
            for pair in pairs:
                if pair[0] + pair[1] == self._port_numbers[curr_index]:
                    break
            else:
                return self._port_numbers[curr_index]
        return None

    def encryption_weakness(self):
        num = self.first_number_not_compliant()
        for index in range(len(self._port_numbers)):
            for i in range(index+1,len(self._port_numbers)):
                num_sum = sum(self._port_numbers[index:i])
                if num_sum == num:
                    max_num = max(self._port_numbers[index:i])
                    min_num = min(self._port_numbers[index:i])
                    return max_num + min_num
                elif num_sum > num:
                    break
        return None