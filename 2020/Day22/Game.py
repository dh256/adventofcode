class Game:

    def __init__(self,input_file):
        # create player decks
        self.decks = []
        with open(input_file, "r") as game_data:
            current_player = 0
            for line in game_data:
                line = line.strip('\n')
                if len(line) > 0:
                    if line.startswith('Player'):
                        current_player += 1
                        self.decks.append([])
                    else:
                        # add card to current player's deck
                        self.decks[current_player-1].append(int(line))

    def _play_round(self):
        card1 = self.decks[0].pop(0)
        card2 = self.decks[1].pop(0)
        if card1 > card2:
            self.decks[0].append(card1)
            self.decks[0].append(card2)
        elif card2 > card1:
            self.decks[1].append(card2)
            self.decks[1].append(card1)
        else: 
            print('Game state invalid - game will terminate')
            exit()

    def _calculate_score(self):
        # who won?
        winner = 0
        if len(self.decks[1]) > 0:
            winner = 1

        # calculate score
        score = 0
        mult = len(self.decks[winner])
        for c in self.decks[winner]:
            score += c * mult
            mult -= 1
        return score
    
    def play(self):
        while len(self.decks[0]) and len(self.decks[1]) > 0:
            self._play_round()
        return self._calculate_score()

    def show_decks(self):
        output = ""
        current_player = 0
        for d in self.decks:
            current_player += 1
            output += f'\nPlayer {current_player}:\n'
            for c in d:
                output += f'{c}\n'
        return output

