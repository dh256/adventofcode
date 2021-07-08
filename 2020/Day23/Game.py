class Game:

    def __init__(self,cup_labels):
        # use a dictionary to link label to next label
        self.num_cups = len(cup_labels)
        self.min_label = min(cup_labels)
        self.max_label = max(cup_labels)
        self.current = cup_labels[0]
        self.cups = {}
        for i,c in enumerate(cup_labels,1):
            if i < self.num_cups:
                self.cups[c] = cup_labels[i]
            else:
                self.cups[c] = cup_labels[0]

    def play(self,moves):
        for move in range(moves):
            # pick ups
            pick_ups = []
            next_cup = self.current
            for i in range(3):
                pick_ups.append(self.cups[next_cup])
                next_cup = self.cups[next_cup]
            self.cups[self.current] = self.cups[pick_ups[2]]

            # calculate destination
            destination = self.current-1 
            while destination == 0 or destination in pick_ups:
                if destination < self.min_label:
                    destination = self.max_label
                else:
                    destination -= 1
            
            # insert pick_ups back into cup circle
            self.cups[pick_ups[2]] = self.cups[destination]
            self.cups[destination] = pick_ups[0]

            # move to next cup
            self.current = self.cups[self.current]
            
        
    def play_part1(self,moves):
        self.play(moves)
        # result
        self.current = 1
        output = ""
        for i in range(self.num_cups - 1):
            output += f'{self.cups[self.current]}'
            self.current = self.cups[self.current]
        return output

    def play_part2(self,moves):
        # play games
        self.play(moves)
        
        # result
        mult1 = self.cups[1]
        mult2 = self.cups[mult1]
        return mult1 * mult2