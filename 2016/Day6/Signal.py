import numpy as np

class Signal:

    def __init__(self, input_file):
        with open(input_file,"r") as file_input:
            first_line = True
            for line in file_input:
                chars = [[c for c in line.strip('\n')]]
                if first_line:
                    self.signal = np.array(chars)
                    first_line = False
                else:
                    self.signal = np.concatenate((self.signal,chars))

    def get_repeating_message(self,most_common=True):
        repeating_message = ""
        for column in self.signal.T:
            letter_distr = {}
            for c in column:
                if c in letter_distr.keys():
                    letter_distr[c] += 1
                else:
                    letter_distr[c] = 1
            repeating_message += [x[0] for x in sorted(letter_distr.items(),key=lambda d : d[1],reverse=most_common)][0]   

        return repeating_message 