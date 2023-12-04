import re
from dataclasses import dataclass, field, InitVar

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
                self.org_cards[id] = Card(id, winners, selected)                   # useful for part 2, quick way of finding cards to copy

    def calc_points(self) -> int:
        '''
        Calculate points value of all scrarchcards
        '''
        return sum([card.points for card in self.cards])
    

    def calc_total_cards(self) -> int:
        '''
        Part 2: calculate total of number of cards left
        Note: Could be more efficient but will do for now
        '''
        for curr_card in range(1,len(self.org_cards)+1):
            # find all cards with an id of curr_cards
            for card in list(filter(lambda card: card.id == curr_card, self.cards)):
                matches = card.matches
                # copy cards
                for c in range(curr_card+1,curr_card+matches+1):  
                    self.cards.append(self.org_cards[c])
        return len(self.cards)