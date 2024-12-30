
''' 
David Hanley, December 2024
'''
from dataclasses import dataclass
from enum import StrEnum, auto
from collections import deque

class GateOp(StrEnum):
    AND = auto()
    OR = auto()
    XOR = auto()

@dataclass
class Gate:
    op: GateOp
    in_wire1: str
    in_wire2: str

class Day24:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        mode: int = 0           # initial wire values
        self.wires: dict[str,bool] = dict()         # hold values of wires
        self.gates: dict[str, Gate] = dict()        # hold each gate, indexed by output wire
        for line in lines:
            if len(line) == 0:
                mode = 1            # change moide to gates and ignore line
                continue
            
            if mode == 0:
                wire, value = line.split(': ')
                self.wires[wire] = bool(int(value))
            else:
                in_wire1, op, in_wire2, _, out_wire = line.split(' ')
                self.gates[out_wire] = Gate(GateOp(op.lower()), in_wire1, in_wire2)
                
                 
        
    def part1(self) -> int:
        '''
        Part 1:
            Create a Q of all output wires whose value need to calculate
            Pull next output wire off Q. If values for both input wires exist, calculate value of output wire
            Otherwise place output wire back into Q
            Continue processing output wires until none left (i.e. they all have a value)
            
            Then, filter all zN wires (where N is an integer label) and sort in descending order (by N)
            Then, convert to a decimal number. For each "bit", if bit is True (1), work out pow(2, <index>) and add to number. 
        '''
        q = deque()
        for out_wire in self.gates.keys():
            q.append(out_wire)
            
        while len(q) > 0:
            next_out_wire = q.popleft()
            gate = self.gates[next_out_wire]
            if gate.in_wire1 in self.wires.keys() and gate.in_wire2 in self.wires.keys():
                if gate.op == GateOp.AND:
                    self.wires[next_out_wire] = self.wires[gate.in_wire1] & self.wires[gate.in_wire2]
                elif gate.op == GateOp.OR:
                    self.wires[next_out_wire] = self.wires[gate.in_wire1] | self.wires[gate.in_wire2]
                elif gate.op == GateOp.XOR:
                    self.wires[next_out_wire] = self.wires[gate.in_wire1] ^ self.wires[gate.in_wire2]
            else:
                q.append(next_out_wire)
        
        # get 'z' wires sorted with highest labelled wire first
        z_wires = sorted(filter(lambda i: i[0].startswith('z'), self.wires.items()),key=lambda t: int(t[0].lstrip('z')), reverse=True)
        
        # convert to decimal
        result: int = 0
        exp: int = len(z_wires)-1
        for _, value in z_wires:
            if value:
                result += pow(2, exp)
            exp -= 1        
        
        return result
        

    def part2(self) -> int:
        return 0
                        
