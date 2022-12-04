import re

class Space:
    def __init__(self,file_name) -> None:
        regex = re.compile(r'\d+')
        self.pairs = list()
        with open(file_name,'r') as input_file:
            for line in input_file:
                nums = regex.findall(line.strip('\n')) 
                set1 = {n for n in range(int(nums[0]),int(nums[1])+1)}
                set2 = {n for n in range(int(nums[2]),int(nums[3])+1)}
                self.pairs.append((set1,set2))

    def pairs_contained_within(self) -> int:
        return len([p for p in self.pairs if p[0].issubset(p[1]) or p[1].issubset(p[0])])

    def pairs_overlap_at_all(self) -> int:
        return len([p for p in self.pairs if len(p[0].intersection(p[1])) > 0])