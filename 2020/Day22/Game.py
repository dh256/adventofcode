from copy import deepcopy

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

    def player_deck(self,player):
        return self.decks[player-1]

    def _play_round(self,card1,card2):
        # play round
        # if card 1 higher, Player 1 wins; otherwise Player 2
        if card1 > card2:
            return 1
        elif card2 > card1:
            return 2

    def calculate_score(self,deck):
        # calculate score
        score = 0
        mult = len(deck)
        for c in deck:
            score += c * mult
            mult -= 1
        return score

    '''
    Play game - return winner and their decks
    '''
    def play_game(self,player1,player2,game=1):             
        prev_rounds = {}   # key is round; value is tuple with player1 and player2 hash
        
        round = 1
        while True:    
            # check whether we have a winner
            # if Player 1 has empty deck, player 2 wins
            # if Player 2 has empty deck, player 1 wins
            if len(player1) == 0:
                return (2,player2)
            
            if len(player2) == 0:
                return (1,player1)

            # Check whether the decks are equal to any previous rounds in this game
            # If so, Player 1 wins this game; if not, continue
            key = str(player1)+str(player2)
            if key in prev_rounds:
                return (1,player1)
            
            prev_rounds[key] = None
        
            # take first two cards
            card1 = player1.pop(0)
            card2 = player2.pop(0)
            
            '''
            For Part2 need to put in an additional check here
            
            If both players have at least as many cards remaining in their 
            deck as the value of the card they just drew, the winner of the 
            round is determined by playing a new game of Recursive Combat
            '''
            if len(player1) >= card1 and len(player2) >= card2:
                # new game - recurse
                winner = self.play_game(player1[:card1],player2[:card2],game+1)[0]
            else:
                winner = self._play_round(card1,card2)

            # winner gets cards    
            if winner == 1:
                player1.extend([card1,card2])
            else:
                player2.extend([card2,card1])
            round += 1
        
    def show_deck(self,deck,player):
        output = ""
        for d in deck:
            output += f'\nPlayer {player}:\n'
            for c in d:
                output += f'{c}\n'
        return output

