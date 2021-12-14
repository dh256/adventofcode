class Polymer:
    def __init__(self,filename):
        
        with open(filename,'r') as input_file:
            lines = [line.strip('\n') for line in input_file]  
        self.template = lines[0]
        self.insertion_rules = {parts[0]: parts[1] for parts in [rule.split(' -> ') for rule in lines[2:]]}
      

    '''
    This method is inefficient. Fine for Part 1 (10 iterations) but won't scale to Part 2 (40 iterations)
    '''
    '''
    def grow_polymer(self,steps):
        for step in range(0,steps):
            # get all the pairs
            pairs = [self.template[index:index+2] for index in range(0,len(self.template)-1)]
            
            # for each pair, look up insertion rule and insert element after first item in pair
            # when done add on last element of polyment
            self.template = f"{''.join([f'{pair[0]}{self.insertion_rules[pair]}' for pair in pairs])}{self.template[-1]}"
            

    def element_difference(self,steps):
        # grow polymer
        self.grow_polymer(steps)
        
        # get distribution of elements
        distribution = {}
        for c in self.template:
            if c in distribution:
                distribution[c] += 1
            else:
                distribution[c] = 1

        return max(distribution.values()) - min(distribution.values())
    '''    

    def element_difference2(self,steps):
        '''
        Work out a pair distribution by continually splitting pairs into their new pairs
        '''
        
        pair_dist = {rule: 0 for rule in self.insertion_rules.keys()}
        
        # set up initial pairs based on template
        for pair in [self.template[index:index+2] for index in range(0,len(self.template)-1)]:
            pair_dist[pair] += 1

        # go round
        for _ in range(0,steps):
            pairs = list(filter(lambda i: i[1] > 0, pair_dist.items()))
            for (k,v) in pairs:
                pair_dist[k] -= v
                new_element = self.insertion_rules[k]
                pair_dist[f'{k[0]}{new_element}'] += v
                pair_dist[f'{new_element}{k[1]}'] += v
        
        # at this point now know pair distribution
        # total up all elements to get element distribution
        elem_dist = {elem: 0 for elem in set(self.insertion_rules.values())}
        for (k,v) in pair_dist.items():
            elem_dist[k[0]] += v
            elem_dist[k[1]] += v
        
        # now each element appears exactly twice (except those at either end which only appear once). So divide total by 2 (except odd where round up by 1)
        for (k,v) in elem_dist.items():
            if v % 2 == 1:
                elem_dist[k] = elem_dist[k] // 2 + 1 
            else:
                elem_dist[k] = elem_dist[k] // 2

        return max(elem_dist.values()) - min(elem_dist.values())