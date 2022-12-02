from Game import Game

def main():
    game = Game('input.txt',1)
    print(f'Strategy 1: {game.play()}')

    game = Game('input.txt',2)
    print(f'Strategy 2: {game.play()}')

if __name__ == '__main__':
    main()