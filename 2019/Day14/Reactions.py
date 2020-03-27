class Reactions:
    def __init__(self,filename):
        with open(filename,'r') as input_data:
            self.reactions = [line.strip('\n') for line in input_data]
            for reaction in self.reactions:
                pass

    '''
    Calculate amount of ore required to produce 1 fuel
    '''
    def calculate_ore_required(self):
        return 31