class Adapters():

    def __init__(self,file_name):
        with open(file_name,'r') as adapter_data:
            self._adapters = [int(line.strip('\n')) for line in adapter_data]
        self._adapters.append(0)
        self._adapters.append(max(self._adapters) + 3)
        self._adapters.sort()

    @property
    def built_in(self):
        return self._adapters[-1]

    def part1(self):
        ones_count = 0
        threes_count = 0        # there is always at least 1, the gap between highest adapter 
        curr_rating = 0
        for index in range(0, len(self._adapters)):
            if self._adapters[index] - curr_rating == 1:
                ones_count += 1
            elif self._adapters[index] - curr_rating == 3:
                threes_count += 1
            curr_rating = self._adapters[index]
        return ones_count * threes_count

    # got stuck
    # Solution found here: https://www.youtube.com/watch?v=eeYanhLamjg 
    # Based on graph theory.
    def part2(self):
        paths = [0] * (max(self._adapters) + 1)
        paths[0] = 1
        for index in range(1, max(self._adapters) + 1):
            for x in range(1,4):
                if (index - x) in self._adapters:
                    paths[index] += paths[index - x]
        return paths[-1]
