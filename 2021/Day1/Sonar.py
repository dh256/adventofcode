class Sonar:

    def __init__(self, filename) -> None:
        with open(filename, "r") as input_file:
            self.depths = [int(line.strip('\n')) for line in input_file]

    @property
    def increased(self):
        inc = 0
        for curr_idx in range(0,len(self.depths)-1):
            if self.depths[curr_idx+1] > self.depths[curr_idx]:
                inc += 1
        return inc   

    @property
    def increased2(self):
        inc = 0
        curr_slide_window = self.depths[0] + self.depths[1] + self.depths[2]
        for curr_idx in range(0,len(self.depths)-3):
            next_slide_window = self.depths[curr_idx+1] + self.depths[curr_idx+2] + self.depths[curr_idx+3]
            if next_slide_window > curr_slide_window:
                inc += 1
            curr_slide_window = next_slide_window
        return inc     
    