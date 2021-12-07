class Crabs:

    def __init__(self,filename):
        with open(filename,'r') as input_file:
            self.positions = [int(pos) for pos in input_file.readline().strip('\n').split(',')]
            self.min_pos = min(self.positions)
            self.max_pos = max(self.positions)


    def align(self):
        '''
        Deternines which horizontal position to align all crabs to using the least amount of fuel, Part 1
        '''
        min_fuel_used = None
        min_fuel_used_pos = None
        for curr_pos in range(self.min_pos,self.max_pos+1):
            # check that this pos
            fuel_used = 0
            for pos in self.positions:
                fuel_used += abs(pos-curr_pos)
            
            # determine if least amount of fuel used
            if min_fuel_used is None or fuel_used < min_fuel_used:
                min_fuel_used = fuel_used
                min_fuel_used_pos = curr_pos

        return (min_fuel_used_pos,min_fuel_used)

    def align2(self):
        '''
        Deternines which horizontal position to align all crabs to using the least amount of fuel, Part 2
        '''
        min_fuel_used = None
        min_fuel_used_pos = None
        for curr_pos in range(self.min_pos,self.max_pos+1):
            fuel_used = 0
            for pos in self.positions:
                diff = abs(pos-curr_pos)
                fuel_used += sum(range(1,diff+1))
            
            # determine if least amount of fuel used
            if min_fuel_used is None or fuel_used < min_fuel_used:
                min_fuel_used = fuel_used
                min_fuel_used_pos = curr_pos

        return (min_fuel_used_pos,min_fuel_used)