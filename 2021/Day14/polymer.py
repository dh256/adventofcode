class Polymer:
    def __init__(self,filename):
        
        with open(filename,'r') as input_file:
            lines = [line.strip('\n') for line in input_file]  
        self.polymer = lines[0]
        self.insertion_rules = {parts[0]: parts[1] for parts in [rule.split(' -> ') for rule in lines[2:]]}

    def grow_polymer(self,steps):
        for step in range(0,steps):
            print(f'Step: {step}')
            
            # get all the pairs
            pairs = [self.polymer[index:index+2] for index in range(0,len(self.polymer)-1)]
            
            # for each pair, look up insertion rule and insert element after first item in pair
            # when done add on last element of polyment
            self.polymer = f"{''.join([f'{pair[0]}{self.insertion_rules[pair]}' for pair in pairs])}{self.polymer[-1]}"

    def element_difference(self,steps):
        # grow polymer
        self.grow_polymer(steps)
        
        # get distribution of elements
        distribution = {}
        for c in self.polymer:
            if c in distribution:
                distribution[c] += 1
            else:
                distribution[c] = 1

        return max(distribution.values()) - min(distribution.values())
        