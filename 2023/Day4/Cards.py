import re
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Card:
    id: int
    winners: set[int]
    selected: set[int]

    @property
    def points(self) -> int:
        matches = self.winners.intersection(self.selected)
        return pow(2, len(matches)-1) if len(matches) > 0 else 0

    @property
    def matches(self) -> int:
        return len(self.winners.intersection(self.selected))

class Cards:
    def __init__(self, file_name) -> None:
        self.cards: list[Card] = []
        self.org_cards: dict = dict()
        with open(file_name,'r') as input_file:
            for line in input_file:
                nums_re = re.compile('\d+')
                parts = line.split(':')
                id = int(re.search(nums_re, parts[0]).group(0))
                nums = parts[1].split('|')
                winners = {int(d) for d in re.findall(nums_re, nums[0])}
                selected = {int(d) for d in re.findall(nums_re, nums[1])}
                self.cards.append(Card(id, winners, selected))
                
    def calc_points(self) -> int:
        '''
        Calculate points value of all scrarchcards
        '''
        return sum([card.points for card in self.cards])
    

    def calc_total_cards(self) -> int:
        '''
        Part 2: calculate total of number of cards left
        More efficient version - just keep a running total of cards and sum these together
        '''
        card_totals = defaultdict(int)
        for card in self.cards:
            card_totals[card.id] += 1
            matches = card.matches
            for c in range(card.id+1,card.id+matches+1):
                card_totals[c] += card_totals[card.id]
        return sum(card_totals.values())