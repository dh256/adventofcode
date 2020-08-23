import re
from enum import Enum

class BotGiveError(Exception):
    '''
        Raised when a Bot cannot give a chip because it does not hold 2 chips
    '''
    pass

class InstructionType(Enum):
    GET_CHIP = 1,
    GIVE_CHIP = 2

class Instruction:
    def __init__(self,instruction):
        self.processed = False
        regex = re.compile(r'(\w+ \d+)')
        if instruction.startswith('value'):
            # bot gets chip
            self.type = InstructionType.GET_CHIP
            results = regex.findall(instruction)
            if len(results) == 2:
                self.bot = int(results[1].split(' ')[1])
                self.chip = int(results[0].split(' ')[1])
            else:
                raise ValueError
        else:
            # bot gives it low and high chips to another bot or output bin
            self.type = InstructionType.GIVE_CHIP
            results = regex.findall(instruction)
            if len(results) == 3:
                # first group in match is a bot number
                self.bot = int(results[0].split(' ')[1])

                # second group is where to put low chip - either to another Bot or Output Bin
                components = results[1].split(' ')
                self.low_dest = components[0]
                self.low_dest_number = int(components[1])

                # third group is where to put high chip - either to another Bot or Output Bin
                components = results[2].split(' ')
                self.high_dest = components[0]
                self.high_dest_number = int(components[1])
            else:
                raise ValueError

class Bot:
    def __init__(self):
        self.low = None
        self.high = None

    def loaded(self):
        return self.low != None and self.high != None
    
    def receive(self, chip_number):
        if self.low == None and self.high == None:
            self.low = chip_number
        elif self.high == None and chip_number >= self.low:
            self.high = chip_number
        elif self.high == None and chip_number < self.low:
            self.high = self.low
            self.low = chip_number
        else: 
            raise ValueError

    def give(self, low_to, high_to):
        if self.low == None or self.high == None:
            raise BotGiveError(f'{self.number} does not contain 2 chips')
        low_to.receive(self.low)
        self.low = None
        high_to.receive(self.high)
        self.high = None

class Output:
    def __init__(self):
        self.chips = []

    def receive(self, chip_number):
        self.chips.append(chip_number)

class Factory:
    def __init__(self,file_name):
        self.outputs = {}
        self.bots = {}
        with open(file_name, "r") as file_input:
            self.instructions = [Instruction(l.strip('\n')) for l in file_input]

    def run(self,compare_vals=None):
        bot_found = False
        bot_found_num = None
        
        if compare_vals[0] > compare_vals[1]:
            self.low_value = compare_vals[1]
            self.high_value = compare_vals[0]
        else:
            self.low_value = compare_vals[0]
            self.high_value = compare_vals[1] 
        
        # load initial chips to Bots
        # after each one check if any bots contain low_value and high_value 
        for instruction in list(filter(lambda i: i.type == InstructionType.GET_CHIP, self.instructions)):
            if not instruction.bot in self.bots:
               self.bots[instruction.bot] = Bot()
            self.bots[instruction.bot].receive(instruction.chip)
            instruction.processed = True
            if not bot_found:
                bot_found_num = self.check_bots()
                if not bot_found_num is None:
                    bot_found = True
                     

        # start to process
        # get loaded Bots  
        # for each loaded Bot, get instructions for this bot
        # after each one check if any bots contain low_value and high_value until one found
        # continue until there are no loaded bots or no more instructions to process
        loaded_bots = list(filter(lambda b: b[1].loaded(), self.bots.items()))
        while len(loaded_bots) > 0 and self.instructions_to_process():
            b = loaded_bots[0]
            for i in list(filter(lambda i: i.type == InstructionType.GIVE_CHIP and i.bot == b[0] and not i.processed, self.instructions)):                
                low_to = self.move_to(i.low_dest, i.low_dest_number)
                high_to = self.move_to(i.high_dest, i.high_dest_number)
                b[1].give(low_to,high_to)
                i.processed = True
                if not bot_found:
                    bot_found_num = self.check_bots()
                    if not bot_found_num is None:
                        bot_found = True
            loaded_bots = list(filter(lambda b: b[1].loaded(), self.bots.items()))

        return (bot_found_num,self.outputs[0].chips[0] * self.outputs[1].chips[0] * self.outputs[2].chips[0]) 

    def check_bots(self):
        result = list(filter(lambda b: b[1].low == self.low_value and b[1].high == self.high_value,self.bots.items()))
        if result == []:
            return None
        else:
            return result[0][0]

    def instructions_to_process(self):
        return len(list(filter(lambda i: not i.processed, self.instructions))) > 0 

    def move_to(self,dest,dest_num):
        if dest == "bot":
            if not dest_num in self.bots:
                self.bots[dest_num] = Bot()
            return self.bots[dest_num]
        else:
            if not dest_num in self.outputs:
                self.outputs[dest_num] = Output()
            return self.outputs[dest_num]