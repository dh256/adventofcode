from Puzzle import Puzzle

'''
screen_width=7
screen_height=3
puzzle = Puzzle("test1.txt",screen_width=screen_width,screen_height=screen_height)
'''
screen_width=50
screen_height=6
puzzle = Puzzle("input.txt",screen_width=screen_width,screen_height=screen_height)

print(f'Pixels Lit: {puzzle.run()}')
print(puzzle)