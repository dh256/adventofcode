class Game:
    board_spaces = 10
    dice_sides = 100
    dice_throws = 3
    winning_score = 1000

    def __init__(self, player1_start, player2_start):
        self.player1_start = player1_start
        self.player2_start = player2_start

    def play(self):
        player1_pos = self.player1_start
        player2_pos = self.player2_start
        player1_total = 0
        player2_total = 0
        dice_val = 1
        total_throws = 0
        while True:
            # player 1 moves
            moves, dice_val, total_throws = self.throw_dice(dice_val,total_throws)     
            player1_pos = self.new_player_position(player1_pos,moves)
            player1_total += player1_pos
            if player1_total >= Game.winning_score:
                winner = 1
                break

            # player 2 moves 
            moves, dice_val, total_throws = self.throw_dice(dice_val,total_throws) 
            player2_pos = self.new_player_position(player2_pos,moves)
            player2_total += player2_pos
            if player2_total >= Game.winning_score:
                winner = 2
                break
            
        loser_score = player2_total if winner == 1 else player1_total
        return loser_score * total_throws
            
    def new_player_position(self,pos,moves):
        pos += moves
        if pos % Game.board_spaces == 0:
            pos = pos - ((pos // Game.board_spaces) - 1) * Game.board_spaces 
        else:
            pos = pos - (pos // Game.board_spaces) * Game.board_spaces 
        return pos

    def throw_dice(self,val,total_throws):
        throws = []
        for _ in range(0,Game.dice_throws):
            # Need to make sure dice wraps back to 1 if > 100
            if val % Game.dice_sides == 0:
                val = val - ((val // Game.dice_sides)-1) * Game.dice_sides 
            else:
                val = val - (val // Game.dice_sides) * Game.dice_sides 
            throws.append(val)
            val += 1
            
        return sum(throws), val, total_throws + Game.dice_throws

    def play2(self):
        return 0