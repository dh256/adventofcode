from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Lens:
    label: str
    focal_len: int

    def __eq__(self, __value: object) -> bool:
        if type(_Lens__value) == str:
            return self.label == __value
        else:    
            return self.label == __value.label

class Hash:
    def __init__(self, file_name) -> None:
        with open(file_name,'r') as input_file:
            self.steps = input_file.readline().strip().split(',') 

    def part1(self) -> int:
        return sum([self.calc_hash(step) for step in self.steps])
        
    def calc_hash(self, label: str) -> int:
        hash_val = 0
        for c in label:
            hash_val += ord(c) 
            hash_val *= 17
            hash_val %= 256
        return hash_val

    def part2(self) -> int:
        boxes: dict = defaultdict(list)
        for step in self.steps:
            if step[-1] == '-':
                # remove lens (if it exists)
                label = step[0:-1]
                box = self.calc_hash(label)
                try:
                    boxes[box].remove(label)
                except ValueError:
                    pass
            else:
                label = step[0:-2]
                box = self.calc_hash(label)
                focal_len = int(step[-1])
                try:
                    idx = boxes[box].index(label)
                    boxes[box][idx] = Lens(label, focal_len)
                except ValueError:
                    boxes[box].append(Lens(label, focal_len))
                    
        # calculate focusing power
        focus_power = 0
        for box in boxes.keys():
            for slot, lens in enumerate(boxes[box], 1):
                focus_power += (box+1) * slot * lens.focal_len
        return focus_power