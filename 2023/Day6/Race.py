import re

class Race:
    def __init__(self,filename) -> None:
        with open(filename,'r') as input_file:
            self.times = [int(num) for num in re.findall('\d+',input_file.readline())]
            self.distances = [int(num) for num in re.findall('\d+',input_file.readline())]           
            self.races = len(self.times)

    def ways_to_win(self,race_duration: int, race_record: int) -> int:
        result = 0
        for presses in range(race_duration):
            v = presses
            t = race_duration - presses
            d = v*t
            if d > race_record:
                result += 1
        return result
    
    def part1(self) -> int:
        result = 1
        for race in range(self.races):
            ways_to_win = self.ways_to_win(self.times[race],self.distances[race])
            result *= ways_to_win if ways_to_win > 0 else 1
        return result

    def part2(self) -> int:
        race_record = int(''.join([str(s) for s in self.distances]))
        race_duration = int(''.join([str(s) for s in self.times]))
        return self.ways_to_win(race_duration, race_record)