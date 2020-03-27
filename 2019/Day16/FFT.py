class FFT:
    def __init__(self,filename):
        self._base_pattern = [0,1,0,-1]
        self._repeating_groups = {}
        with open(filename,"r") as file_in:
            self.fft_input = file_in.readline().strip('\n')

    def run(self, phases):
        elements = self.fft_input
        for p in range(0,phases):
            element = 0
            results = []
            for e in range(0,len(elements)):
                repeating_group = self._get_repeating_group(e)
                group_sum = 0
                index = 1
                for d in elements:
                    if index > len(repeating_group)-1:
                        index = 0
                    group_sum += int(d) * int(repeating_group[index])
                    index += 1
                results.append(abs(group_sum) % 10)
            elements = results

        return ''.join([str(elem) for elem in elements[:8]]) 

    def _get_repeating_group(self,e):
        if self._repeating_groups.get(e,None) == None:
            # repeating group not created before, create
            repeating_group = []
            for v in self._base_pattern:
                repeating_group += [v] * (e+1)
            self._repeating_groups[e] = repeating_group
        
        # return repeating group
        return self._repeating_groups.get(e)

