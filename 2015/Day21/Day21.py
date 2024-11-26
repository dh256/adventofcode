'''
David Hanley, November 2024
'''
import re
from dataclasses import dataclass
from itertools import combinations,permutations,product

@dataclass
class PlayerStats:
    hit_points: int
    damage: int
    armour: int
    
@dataclass
class ItemStats:
    cost: int
    damage: int
    armour: int

@dataclass 
class Permutation:
    weapon: str
    chosen_armour: None | str
    rings: None | list[str]
    cost: int
    damage: int
    armour: int

@dataclass
class GamePermutations:
    # Class that handles game permutations (weapons, armour and rings)
    # you can have at most one weapon
    # you can have zero or more armor
    # you can have 0-2 rings (no duplicates)
    # work out all possible permutation and calculate cost, damage and defence of of each combination
    def __init__(self) -> None:
        self._weapons: dict[str, ItemStats] = {'Dagger': ItemStats(8,4,0),
                                 'Shortsword':ItemStats(10,5,0),
                                 'Warhammer':ItemStats(25,6,0),
                                 'Longsword':ItemStats(40,7,0),
                                 'Greataxe':ItemStats(74,8,0)}

        self._armour: dict[str, ItemStats] = {'Leather':ItemStats(13,0,1),
                                'Chainmail':ItemStats(31,0,2),
                                'Splintmail':ItemStats(53,0,3),
                                'Bandedmail':ItemStats(75,0,4),
                                'Platemail':ItemStats(102,0,5)}

        self._rings: dict[str, ItemStats] = {'Damage +1':ItemStats(25,1,0),
                                'Damage +2':ItemStats(50,2,0),
                                'Damage +3':ItemStats(100,3,0),
                                'Defense +1':ItemStats(20,0,1),
                                'Defense +2':ItemStats(40,0,2),
                                'Defense +3':ItemStats(80,0,3)}

        # work our permutations, sorted by cost
        weapons_list = [k for k in self._weapons.keys()]
        armour_list = [k for k in self._armour.keys()] + [None]
        rings_list = [k for k in self._rings.keys()]
        rings_list = rings_list + list(combinations(rings_list,2)) + [None]
        item_permutations = product(weapons_list,armour_list,rings_list)
        
        # calculate cost, damage and armour for each permutation
        self._permutations: list[Permutation] = list()
        for item_perm in item_permutations:
            # calculate cost, defence, damage
            cost = 0
            damage = 0
            armour = 0
            cost += self._weapons[item_perm[0]].cost 
            damage += self._weapons[item_perm[0]].damage 
            if item_perm[1]:
                cost += self._armour[item_perm[1]].cost
                armour += self._armour[item_perm[1]].armour 
            
            rings: list[str] = None 
            if item_perm[2]:
                if type(item_perm[2]) == str:
                    rings = [item_perm[2]]
                else:
                    rings = list(item_perm[2])
                for ring in rings:
                    if ring:
                        cost += self._rings[ring].cost
                        damage += self._rings[ring].damage 
                        armour += self._rings[ring].armour 

            self._permutations.append(Permutation(item_perm[0],item_perm[1],rings,cost,damage,armour))
        
    def permutations(self,part: int) -> list[Permutation]:
        # sort by cost in ascending order (part 1); descending order (part 2)
        return sorted(self._permutations,key=lambda p: p.cost, reverse=part == 2)

class Day21:
    def __init__(self,file_name:str) -> None:
        # read in bosses stats
        with open(file_name, 'r') as input_file:
            nums = [re.findall(r'\d+',line.strip('\n')) for line in input_file]
            
        for i, num in enumerate(nums):
            if i == 0:
                self._boss_hit_points = int(num[0])
            elif i == 1:
                self._boss_damage = int(num[0])
            elif i == 2:
                self._boss_armour = int(num[0])
        
        # dictionary to hold players
        self.players: dict[int, PlayerStats] = dict()
    
    def _turn(self, attacker: int, defender: int) -> int:
        attacker_damage:int = self.players[attacker].damage
        defender_armour:int = self.players[defender].armour
        damage_dealt:int = attacker_damage - defender_armour
        damage_dealt = 1 if damage_dealt <= 0 else damage_dealt
        self.players[defender].hit_points -= damage_dealt
    
    def _reset(self,player1_damage,player1_armour) -> None:
        self.players[1] = PlayerStats(100,player1_damage,player1_armour)
        self.players[2] = PlayerStats(self._boss_hit_points,self._boss_damage,self._boss_armour)

    def solution(self) -> list[int]:
        # play game (using each permutations soerted by cost (either asc for part 1 or desc for part 2)) until I (me) wins (part1) or loseds (part2)
        # Returns cost of current permutation for each part
        result: list[int] = list()
        game_perms: GamePermutations = GamePermutations()
        for part in (1,2):
            result.append(self._run_game(part, game_perms))
        return result

    def _run_game(self, part: int,game_perms:GamePermutations) -> int:
        for game_perm in game_perms.permutations(part):
            # reset players 
            self._reset(game_perm.damage,game_perm.armour)
            
            while True:
                self._turn(1,2)
                if self.players[2].hit_points < 1:
                    # player 1 (me) wins
                    if part == 1:
                        return game_perm.cost
                    break
                
                self._turn(2,1)
                if self.players[1].hit_points < 1:
                    # player 1 (me) loses
                    if part == 1:
                        break
                    return game_perm.cost
                        
