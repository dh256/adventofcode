from dataclasses import dataclass
from copy import deepcopy
@dataclass
class Layer:
    range: int
    scanner_pos: int = 0
    scanner_increment: int = 1
    
    def move_scanner(self):
        self.scanner_pos += self.scanner_increment
        if self.scanner_pos == 0:
            self.scanner_increment = 1
        elif self.scanner_pos == self.range-1:
            self.scanner_increment = -1
        
    def reset(self):
        self.scanner_pos = 0
        self.scanner_increment = 1
class Day13:

    def __init__(self, file_name) -> None:
        with open(file_name, 'r') as input_file:
            lines: list[str] = [line.strip('\n') for line in input_file]
        
        # populate layers
        self._layers: dict[int, Layer] = dict()
        for line in lines:
            line_parts = line.split(': ')
            layer_depth: int = int(line_parts[0])
            layer_range: int = int(line_parts[1])
            self._layers[layer_depth] = Layer(layer_range)
        self._max_depth = layer_depth
    
    def reset(self) -> None:
        for k in self._layers.keys():
            self._layers[k].reset()
    
    def _caught_layers(self,part: int) -> list[int]:
        '''
        Returns list of depth of layers where packet is caught
        '''
        caught_layers: list[int] = list()
        for curr_packet_depth in range(0,self._max_depth+1):
            for depth in self._layers.keys():
                # check whether it's a catch
                if depth == curr_packet_depth and self._layers[depth].scanner_pos == 0:
                    if part == 1:
                        caught_layers.append(depth)
                    else:
                        return [0]
                    
                # move scanner and if necessary change increment
                self._layers[depth].move_scanner()
        
        return caught_layers
    
    def part1(self) -> int:
        '''
        Move packet through all layers and record any layers it is caught in
        When complete sum up the depth*range of any caught layer
        '''
        caught_layers: list[int] = self._caught_layers(1)
        return sum(map(lambda d: d * self._layers[d].range, caught_layers))
        
    def part2(self) -> int:
        '''
        Although works is slow. There is a more efficient method
        '''
        depth: int = 0
        while True:
            if depth % 10000 == 0:
                print(depth)
            
            for k in self._layers.keys():
                self._layers[k].move_scanner()
            
            state: dict[int, Layer] = deepcopy(self._layers)
            
            if len(self._caught_layers(2)) == 0:
                return depth + 1
            
            self._layers = state
            depth += 1
            