from dataclasses import dataclass,InitVar,field

@dataclass
class Hand:
    cards: str
    bid: int
    type: int = 1       # default to HIGH CARD
    
    def __post_init__(self):
        # calc type
        card_counts = {card: 0 for card in "23456789TJKQA"}
        for c in self.cards:
            card_counts[c]+=1
        
        # five of a kind
        if len(list(filter(lambda i: i[1] == 5, card_counts.items()))) == 1:
            self.type=7
            return
        
        # four of a kind        
        if len(list(filter(lambda i: i[1] == 4, card_counts.items()))) == 1:
            self.type=6
            return

        # three of a kind or full house
        if len(list(filter(lambda i: i[1] == 3, card_counts.items()))) == 1:
            if len(list(filter(lambda i: i[1] == 2, card_counts.items()))) == 1:
                self.type = 5
            else:
                self.type = 4
            return

        # one pair or two pair
        pairs = list(filter(lambda i: i[1] == 2, card_counts.items()))
        if len(pairs) == 2:
            self.type = 3
        elif len(pairs) == 1:
            self.type = 2

class Camel:
    def __init__(self,file_name) -> None:
        self.hands:list[Hand] = []
        with open(file_name, 'r') as input_file:
            for line in input_file:
                cards, bid = [part for part in line.split(' ')]
                self.hands.append(Hand(cards, int(bid)))


    def total_winnings(self) -> int:
        # sort by type and card value
        # to make sorting easier remap cards so that they in are in ascii order
        for i in range(len(self.hands)):
            c = self.hands[i].cards
            c = c.replace('A','E')
            c = c.replace('T','A')
            c = c.replace('J','B')
            c = c.replace('Q','C')
            c = c.replace('K','D')
            self.hands[i].cards = c

        self.hands = list(sorted(self.hands, key=lambda h: (h.type, h.cards)))
        result = 0
        for (i,c) in enumerate(self.hands,1):
            result += i * c.bid
        return result