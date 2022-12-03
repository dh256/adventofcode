class Rucksack:
    def __init__(self,file_name) -> None:
        with open(file_name,'r') as input_file:
            self.rucksacks = [line.strip('\n') for line in input_file]
                

    def _find_common_item1(self,curr_rucksack: int) -> str:
        '''
        Find item that appears once in each compartment of current racksack
        '''
        comp_items = len(self.rucksacks[curr_rucksack]) // 2
        comp1 = self.rucksacks[curr_rucksack][0:comp_items]
        comp2 = self.rucksacks[curr_rucksack][comp_items:]
        for item in comp1:
            if item in comp2:
                return item

    def _find_common_item2(self,group: int) -> str:
        for item in self.rucksacks[group*3]:
            if item in self.rucksacks[group*3+1] and item in self.rucksacks[group*3+2]:
                return item

    def _item_priority(self, item) -> int:
        '''
        Calculate item priority
        '''
        if ord(item) in range(ord('a'),ord('z')+1):
            return (ord(item) - ord('a')) + 1
        else:
            return (ord(item) - ord('A')) + 27

    def calc_priority_sum(self,item_type: int) -> int:
        '''
        Type 1: Calculate the priority sum of the item that appears in both compartments in each rucksack
        Type 2: Calculate the priority sum of the item that appears at least once in each group of three rucksacks
        '''        
        if item_type == 1:
            return sum([self._item_priority(self._find_common_item1(curr_rucksack)) for curr_rucksack in range(0,len(self.rucksacks))])
        else:
            return sum([self._item_priority(self._find_common_item2(group)) for group in range(0,len(self.rucksacks) // 3)])
        

    