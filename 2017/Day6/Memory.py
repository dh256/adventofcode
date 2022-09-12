import re

class Memory:
    def __init__(self,filename):
        with open(filename,'r') as input_file:
            self.banks = dict(enumerate([int(i) for i in re.findall(r'\d+', input_file.readline())]))
            self.num_banks = len(self.banks)

    def restribute(self,seen_before_events) -> int:
        seen_banks = list()
        seen_banks.append(str(list(self.banks.values())))
        rounds = 0

        while True:
            rounds += 1
            
            # find bank with highest number of blocks
            (idx,blocks) = [t for t in sorted(self.banks.items(), key=lambda i: (i[1], i[0]),reverse=True) if t[1] == max(self.banks.values()) ][-1]
            
            # spread out the banks
            self.banks[idx] = 0
            for bank_idx in range(1,blocks+1):
                self.banks[(idx+bank_idx) % self.num_banks] += 1

            # if seen before, return number of rounds 
            banks = str(list(self.banks.values()))
            if len(list(filter(lambda sb: sb == banks,seen_banks))) == seen_before_events:
                return rounds
            else:
                seen_banks.append(banks)