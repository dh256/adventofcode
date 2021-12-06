class Fish:
    def __init__(self,filename):
        with open(filename,'r') as input_file:
            ages = [int(age) for age in input_file.readline().strip('\n').split(',')]
            
        # create a population breakdown - for each age contains a count of number of fish in this age group. Needed to make this scale
        self.population = {}
        for index in range(0,9):
            self.population[index] = 0
        for age in ages:
            self.population[age] += 1

    # Simulate (good for Parts 1 and 2)
    def simulate(self,days):
        for day in range(1,days+1):
            # remember number in group zero - these will all move to 6 and for each one a new 8 will be added
            # the number in each group moves down one group (8 through 1)
            # group 8 goes to number in group 0
            # group 6 is incremented by number in group 0
            group0 = self.population[0]
            for index in range(1,9):
                self.population[index-1] = self.population[index]
            self.population[8] = group0
            self.population[6] += group0

        # return a sum in all groups
        return sum(self.population.values())
    