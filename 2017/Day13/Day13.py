import re
from dataclasses import dataclass

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
    
    def part1(self) -> int:
        '''
        Move packet through all layers and record any layers it is caught in
        When complete sum up the depth*range of any caught layer
        '''
        caught_layers: int = 0
        for curr_packet_depth in range(0,self._max_depth+1):
            for depth in self._layers.keys():
                # check whether it's a catch
                if depth == curr_packet_depth and self._layers[depth].scanner_pos == 0:
                    caught_layers += depth * self._layers[depth].range
                    
                # move scanner and if necessary change increment
                self._layers[depth].move_scanner()
        
        return caught_layers 
        

    def part2(self) -> int:
        pass
            