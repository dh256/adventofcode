import numpy
import re
from dataclasses import dataclass, InitVar, field
from collections import defaultdict

@dataclass
class SelectedCube:
    colour: str = field(init=False)
    count: int = field(init=False)
    cube_set: InitVar[str]

    def __post_init__(self, selected_cube: str) -> None:
        parts = selected_cube.split(' ')
        self.colour = parts[1]
        self.count = int(parts[0])

class Game:
    bag_contents = {'red': 12, 'blue': 14, 'green': 13}
    def __init__(self, input: str) -> None:
        self.id = int(re.search(r'\d+', input)[0])
        self.subsets = []
        subsets_raw_data = input.split(':')[1].lstrip(' ')
        subset_raw_data = subsets_raw_data.split(';')
        for subset_raw in subset_raw_data:
            selected_cubes = []
            cube_sets_raw = re.findall(r'(\d+ (red|blue|green))',subset_raw)
            for cube_set in cube_sets_raw:
                selected_cubes.append(SelectedCube(cube_set[0]))
            self.subsets.append(selected_cubes)

    @property
    def possible(self) -> bool:
        # not possible if any cube count exceeds max number in bage
        for subset in self.subsets:
            for selected_cube in subset:
                if selected_cube.count > Game.bag_contents[selected_cube.colour]:
                    return False
        return True
    
    @property
    def power(self) -> int:
        # get max number of each cube colour across sets
        num_cubes = defaultdict(int)
        for subset in self.subsets:
            for selected_cube in subset:
                if selected_cube.count > num_cubes[selected_cube.colour]:
                    num_cubes[selected_cube.colour] = selected_cube.count
        
        # calculate power
        return numpy.prod(list(num_cubes.values()))

class Games:
    def __init__(self, filename: str) -> None:
        with open(filename, 'r') as input_file:
            self.games = [Game(line.strip('\n')) for line in input_file]

    def sum_of_impossible_ids(self) -> int:
        result = sum([game.id for game in self.games if game.possible])
        return result
    
    def sum_of_powers(self) -> int:
        result = sum([game.power for game in self.games])
        return result