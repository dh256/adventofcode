from dataclasses import dataclass,InitVar,field

@dataclass
class Hand:
    card_suits = "23456789TJKQA"
    cards: str
    bid: int
    type: int
    
    @staticmethod 
    def calc_type(cards, part):
        # get card counts
        card_counts = {card: 0 for card in Hand.card_suits}
        for c in cards:
            card_counts[c]+=1
        
        # five of a kind
        if len(list(filter(lambda i: i[1] == 5, card_counts.items()))) == 1:
            return 7
        
        if part == 1:
            # four of a kind        
            if len(list(filter(lambda i: i[1] == 4, card_counts.items()))) == 1:
                return 6

            # three of a kind or full house
            if len(list(filter(lambda i: i[1] == 3, card_counts.items()))) == 1:
                if len(list(filter(lambda i: i[1] == 2, card_counts.items()))) == 1:
                    return 5
                else:
                    return 4

            # one pair or two pair
            pairs = list(filter(lambda i: i[1] == 2, card_counts.items()))
            if len(pairs) == 2:
                return 3
            elif len(pairs) == 1:
                return 2

            return 1
        else:
            # four of a kind        
            fours = dict(filter(lambda i: i[1] == 4, card_counts.items()))
            if len(fours) == 1:
                if card_counts['J'] == 4 or card_counts['J'] == 1:
                    return 7
                else:
                    return 6

            # three of a kind or full house
            threes = dict(filter(lambda i: i[1] == 3, card_counts.items()))
            if len(threes) == 1:
                twos = dict(filter(lambda i: i[1] == 2, card_counts.items()))
                
                # 1 pair and 1 3 - 2 or 2 J promote to 5 of a Kind
                if len(twos) == 1 and (card_counts['J'] == 3 or card_counts['J'] == 2):
                    return 7
                # No pair - 3 or 2 J promote to 1 of a Kind
                if len(twos) == 0 and (card_counts['J'] == 3 or card_counts['J'] == 1):
                    return 6
                s
                # full house
                if len(twos) == 1 and card_counts['J'] == 0:
                    return 5
                
                # three of a kind
                return 4

            # one pair or two pair
            pairs = dict(filter(lambda i: i[1] == 2, card_counts.items()))
            if len(pairs) == 2:
                # if one of pairs is a J then promote to four of a kind
                if card_counts['J'] == 2:
                    return 6
                
                if card_counts['J'] == 1:
                    # if a single jack promote to full house
                    return 5
                
                # 2 pairs
                return 3
           
            if len(pairs) == 1:
                # if a single J or 2 Js, promote to 3 of a kind
                if (card_counts['J'] == 1 or card_counts['J'] == 2):
                    return 4
                
                # one pair
                return 2

            if len(pairs) == 0:
                # if a single J promote to one pair
                if card_counts['J'] == 1:
                    return 2

            # High Card 
            return 1


class Camel:
    def __init__(self,file_name:str,part:int) -> None:
        self.part = part
        self.hands:list[Hand] = []
        with open(file_name, 'r') as input_file:
            for line in input_file:
                cards, bid = [part for part in line.split(' ')]
                self.hands.append(Hand(cards, int(bid), Hand.calc_type(cards,self.part)))
                

    def total_winnings(self) -> int:
        # sort by type and card value
        # to make sorting easier remap cards so that they in are in ascii order
        for i in range(len(self.hands)):
            c = self.hands[i].cards
            c = c.replace('A','E')
            c = c.replace('T','A')
            if self.part == 1:
                c = c.replace('J','B')
            else:
                c = c.replace('J','1')
            c = c.replace('Q','C')
            c = c.replace('K','D')
            self.hands[i].cards = c

        self.hands = list(sorted(self.hands, key=lambda h: (h.type, h.cards)))
        result = 0
        for (i,c) in enumerate(self.hands,1):
            result += i * c.bid
        return result