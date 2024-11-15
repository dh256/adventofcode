'''
David Hanley, November 2024
'''

from dataclasses import dataclass

@dataclass
class Reindeer:
    fly_speed: int
    fly_time: int
    rest_time: int
    points: int = 0   # needed for part 2

    def distance_travelled(self, interval: int) -> int:
        """Calculate distance travelled in give time interval (seconds), accounting for rest periods

        Args:
            interval (int): time in seconds

        Returns:
            int: distance travelled (km)
        """
        
        # total flight time available in interval
        full_fly_units_available: int = interval // (self.fly_time + self.rest_time)
        flight_time_available: int = full_fly_units_available * self.fly_time
        fly_time_left_over: int = interval % (self.fly_time + self.rest_time)
        if fly_time_left_over > self.fly_time:
            flight_time_available += self.fly_time
        else:
            flight_time_available += fly_time_left_over

        # calculate distance travelled in flight time available
        return flight_time_available * self.fly_speed

class Day14:
    def __init__(self,file_name:str) -> None:
        self.reindeers: dict[str, Reindeer] = dict()
        with open(file_name, 'r') as input_file:
            inputs = [line.strip('\n').split(' ') for line in input_file]
            
        for input_parts in inputs:
            self.reindeers[input_parts[0]] = Reindeer(int(input_parts[3]), 
                                                      int(input_parts[6]), 
                                                      int(input_parts[13]))
        
    def part1(self, interval: int) -> int:
        """Calculate max distance travelled by any reindeer in given interval

        Args:
            interval (int): time in seconds

        Returns:
            int: max distance travelled
        """
        distances_travelled: list[int] = [v.distance_travelled(interval) for k, v in self.reindeers.items()]
        return sorted(distances_travelled,reverse=True)[0]
        
    def part2(self, interval: int) -> int:
        """Calculate the maximum number of points acrued by any reindeer in given inteval

        Args:
            interval (int): time in seconds

        Returns:
            int: Max number of points acrued
        """
        for elapsed_time in range(1,interval+1):
            interval_results: dict[str, int] = dict()
            for name, r in self.reindeers.items():
                interval_results[name] = r.distance_travelled(elapsed_time)                    
                
            sorted_interval_results: list[tuple[str,int]] = list(sorted([(i[0],i[1]) for i in interval_results.items()], key = lambda l: l[1], reverse=True))
            max_distance: int = sorted_interval_results[0][1]
            for name, distance_travelled in sorted_interval_results:
                if distance_travelled == max_distance:
                    self.reindeers[name].points += 1
                else:
                    break
            
        return sorted([v.points for v in self.reindeers.values()],reverse=True)[0]
                        
