class Bathroom:

    def __init__(self,filename):
        with open(filename,"r") as input_file:
            self.instuctions = [line.strip('\n') for line in input_file]

    def edge(self,x,y):
        return self.keypad[y][x] == ''
    
    def get_keycode(self,part1=True):
        # set up keypad
        if part1:
            self.five_key = (2,2)
            self.keypad = [['','','','',''],['','1','2','3',''],['','4','5','6',''],['','7','8','9',''],['','','','','']]
        else:
            self.five_key = (3,1)
            self.keypad = [ ['','','','','','',''],
                            ['','','','1','','',''],
                            ['','','2','3','4','',''],
                            ['','5','6','7','8','9',''],
                            ['','','A','B','C','',''],
                            ['','','','D','','',''],
                            ['','','','','','','']]
        
        # calculate keycode
        keycode = ""
        x = self.five_key[1]
        y = self.five_key[0]
        for instruction in self.instuctions:
            for move in instruction:
                if move == "U":
                    if not self.edge(x,y-1):
                        y -= 1

                elif move == "D":
                    if not self.edge(x,y+1):
                        y += 1

                elif move == "R":
                    if not self.edge(x+1,y):
                        x += 1

                elif move == "L":
                    if not self.edge(x-1,y):
                        x -= 1

            keycode += self.keypad[y][x]

        return keycode

        