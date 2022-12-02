from enum import Enum

class Material(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

class RoundResult(Enum):
    Win='Z'
    Draw='Y'
    Defeat='X'

class RockPaperScissors:
    
    def __init__(self,code: str):
        if code in ('A', 'X'):
            self.material = Material.Rock
        elif code in ('B', 'Y'):
            self.material = Material.Paper
        elif code in ('C', 'Z'):
            self.material = Material.Scissors
        else:
            print('Corrupt Input. Exiting program')
            exit(-1)

    def compare(self,competitor):
        '''
        Returns 6 if you win, 3 if a draw and 0 if competitor wins + value of material
        '''
        if self.material == competitor.material:
            score = 3
        else:
            if  (self.material == Material.Rock and competitor.material == Material.Scissors) or \
                (self.material == Material.Scissors and competitor.material == Material.Paper) or \
                (self.material == Material.Paper and competitor.material == Material.Rock ):
                score = 6
            else:
                score = 0
        return score + self.material.value

    def other_material(self, result: RoundResult):
        '''
        Determines what other material based on Round Result
        Return instance of other material
        '''
        if self.material == Material.Rock: 
            if result == RoundResult.Win:
                return RockPaperScissors('B')
            elif result == RoundResult.Draw:
                return RockPaperScissors('A')
            else:
                return RockPaperScissors('C')

        elif self.material == Material.Paper:
            if result == RoundResult.Win:
                return RockPaperScissors('C')
            elif result == RoundResult.Draw:
                return RockPaperScissors('B')
            else:
                return RockPaperScissors('A')

        elif self.material == Material.Scissors:
            if result == RoundResult.Win:
                return RockPaperScissors('A')
            elif result == RoundResult.Draw:
                return RockPaperScissors('C')
            else:
                return RockPaperScissors('B')

class Game:
    def __init__(self,file_name,strategy):
        self.rounds = list()
        self.strategy = strategy
        with open(file_name, 'r') as input_file:
            for line in input_file:
                round_instructions = line.strip('\n').split(' ')
                if self.strategy == 1:
                    self.rounds.append((RockPaperScissors(round_instructions[1]),RockPaperScissors(round_instructions[0])))
                else:
                    self.rounds.append((RockPaperScissors(round_instructions[0]),RoundResult(round_instructions[1])))


    def play(self) -> int:
        '''
        Play game and return total score
        '''
        if self.strategy == 1:
            return sum([round[0].compare(round[1]) for round in self.rounds])
        else:
            return sum([round[0].other_material(round[1]).compare(round[0]) for round in self.rounds])

