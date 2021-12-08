import re

class Signal:
    def __init__(self,input_str):
        parts = input_str.split('|')
        self._patterns = [set(p) for p in re.findall(r'\w+',parts[0])]
        self._outputs = [set(o) for o in re.findall(r'\w+',parts[1])]

    @property
    def patterns(self):
        return self._patterns

    @property
    def outputs(self):
        return self._outputs

class Display():
    def __init__(self,filename) -> None:
        with open(filename,'r') as input_file:
            self._signals = [Signal(line.strip('\n')) for line in input_file]            

    def digits_appear(self):
        '''
        Return the number of times 1,4,7 and 8 appear
        '''
        digits_appear = 0
        for signal in self._signals:
            digits_appear += len(list(filter(lambda x : len(x) in (2,3,4,7), signal.outputs)))
        return digits_appear

    def output_sum(self):
        out_sum = 0
        for signal in self._signals:
            # Need to map pattern to gits
            map = self._pattern_to_digit_map(signal.patterns)
            
            # once map complete, generate output
            digits = ''
            for output in signal.outputs:
                digits += str(map.index(output))
            out_sum += int(digits)
        return out_sum

    def _pattern_to_digit_map(self, patterns):
        map_digits = {}

        # map all those with unique length (1,4,7,8)
        map_digits["1"] = list(filter(lambda x : len(x) == 2, patterns))[0]
        map_digits["7"] = list(filter(lambda x : len(x) == 3, patterns))[0]
        map_digits["4"] = list(filter(lambda x : len(x) == 4, patterns))[0]
        map_digits["8"] = list(filter(lambda x : len(x) == 7, patterns))[0]

        len_6 = list(filter(lambda x : len(x) == 6, patterns))
        for p in len_6:
            # 1 is not a subset of 6
            if not map_digits["1"].issubset(p):
                map_digits["6"] = p
            # 4 is a subset of 9
            elif map_digits["4"].issubset(p):
                map_digits["9"] = p
            # only zero remains
            else:
                map_digits["0"] = p
        
        # now find all patters with length 5
        len_5 = list(filter(lambda x : len(x) == 5, patterns))
        for p in len_5:
            # 7 is a subset of 3
            if map_digits["7"].issubset(p):
                map_digits["3"] = p
            # 5 is a subset of 6
            elif p.issubset(map_digits["6"]):
                map_digits["5"] = p
            else:
                # only 2 is left
                map_digits["2"] = p
        
        # change map_digits to a list index 0 is pattern for 0 etc.
        return [map_digits[str(i)] for i in range(0,10)] 