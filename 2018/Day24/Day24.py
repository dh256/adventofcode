from enum import Enum,auto

class ArmyType(Enum):
    IMMUNE=auto()
    INFECTION=auto()


class Units:
    def __init__(self, line):
        # use regex to extract relevant data
        regex = re.match("(\d+)") 
        
        hit_points = 0
        attack_damage = 0
        attack_initiative = 0
        attack_type = 0
        self.hit_points = hit_points
        self.attack_damage = attack_damage
        self.initiative = initiative
        self.attack_type = attack_type

class Group:
    def __init__(self,units):
        self.group_id = None  # populated when added to an army
        self.units = units
        self.effective_power = units.hit_points * units.attack_damage

class Army:
    def __init__(self,type):
        self.type = type
        self.groups = []

    def append(self, group):
        group.group_id = len(self.groups+1)
        self.groups.append(group)

class Game:
    def __init__(self, filename):
        self.immune_army = Army(ArmyType.IMMUNE)
        self.infection_army = Army(ArmyType.INFECTION)

    def _process_input(filename):
        '''
        Process input from file filename
        '''
        mode = None
        with open(filename, 'r') as input:
            for line in input:
                line = line.strip('\n')
                if mode is None and line == 'Immune System:':
                    # process immune system input
                    mode = ArmyType.IMMUNE

                if mode is None and line == 'Infection':
                    # process infection system input
                    mode = ArmyType.INFECTION

                if (mode == ArmyType.INFECTION or mode == ArmyType.IMMUNE) and len(line) == 0:
                    mode = None

    def play(self):
        '''
        Play the game
        '''