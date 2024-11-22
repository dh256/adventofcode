'''
David Hanley, November 2024
'''
class Day20:
    def __init__(self) -> None:
        pass
            
    def get_factors(self, num: int) -> list[int]:
        '''
        Returns all factors of given number.
        This gives the ids of the elves that stop at this house number (num)
        '''        
        i = 1
        factors: list[int] = list()
        while i*i <= num:
            if num % i == 0:
                factors.append(i)
                if num // i != i: 
                    factors.append(num // i)
            i += 1
        return factors
 
    def solution(self, least_presents: int) -> tuple[int, int]:
        '''
        Brute force approach. For each house number, get its factors i.e. the number of each elf that visits house
        Now, calculate the total num of presents:
            For Part 1 multiply each factor (elf id) by 10
            For Part 2 multiply each factor (elf id) by 11 unless elf already visited 50 houses
        Keep going until find total num of presents at least equal to least_presents for parts 1 and 2 return house_number found for each part
        '''
        curr_house = 1
        part1_houses = None
        part2_houses = None
        while part1_houses is None or part2_houses is None:
            elf_ids = self.get_factors(curr_house)
            if part1_houses is None:
                part1_presents = sum([e * 10 for e in elf_ids])
                if part1_presents >= least_presents:
                    part1_houses = curr_house
            
            if part2_houses is None:
                part2_presents = sum([e * 11 for e in elf_ids if curr_house <= e * 50])
                if part2_presents >= least_presents:
                    part2_houses = curr_house
            
            curr_house += 1   
            
        return (part1_houses,part2_houses)     
            
