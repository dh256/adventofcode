class Sonar:

    def __init__(self, filename) -> None:
        with open(filename, "r") as input_file:
            self.depths = [int(line.strip('\n')) for line in input_file]

    @property
    def increased(self):
        return len(['inc' for curr_idx in range(0,len(self.depths)-1) if self.depths[curr_idx+1] > self.depths[curr_idx]])
           
    @property
    def increased2(self):
        return len(['inc' for curr_idx in range(0,len(self.depths)-3) if sum(self.depths[curr_idx:curr_idx+3]) < sum(self.depths[curr_idx+1:curr_idx+4])])