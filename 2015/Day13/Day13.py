'''
David Hanley, Nov 2024
Not the most efficient algorithm but it works in ~30 seconds for Part 2
'''
from itertools import permutations

class Day13:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
           raw_happiness = [line.strip('\n').split(' ') for line in input_file]
        
        # get happiness rules   
        self.happiness: list[tuple[str,int,str]] = list()
        self.attendee_names: set[str] = set()
        for rh in raw_happiness:
            change = int(rh[3]) if rh[2] == 'gain' else int(rh[3]) * -1
            self.happiness.append((rh[0],change,rh[-1][0:-1]))
            self.attendee_names.add(rh[0])
        
        self.attendees: int = len(self.attendee_names)
        
    def _max_impact(self) -> int:
        impacts: list[int] = list()
        for seat_option in permutations(self.attendee_names):
            impact = 0
            for index in range(0,self.attendees):
                # calculate total impact of this arrangement
                sitting_now = seat_option[index % self.attendees]
                sitting_left = seat_option[(index-1) % self.attendees]
                sitting_right = seat_option[(index+1) % self.attendees]
                
                sitting_left_change = list(filter(lambda h: h[0] == sitting_now and h[2] == sitting_left, self.happiness))[0][1]
                sitting_right_change =  list(filter(lambda h: h[0] == sitting_now and h[2] == sitting_right, self.happiness))[0][1]
                impact += sitting_left_change + sitting_right_change
                
            impacts.append(impact) 
        return max(impacts)

    def part1(self) -> int:
        return self._max_impact()
    

    def part2(self) -> int:
        # add myself to the party
        self.attendee_names.add('You')
        self.attendees += 1
        for name in self.attendee_names:
            self.happiness.append(('You',0,name))
            self.happiness.append((name,0,'You'))
            
        # calculate maximum impact now
        return self._max_impact()
                        
