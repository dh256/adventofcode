from Game import Games

def main():
    games = Games('input.txt')
    print(games.sum_of_impossible_ids())
    print(games.sum_of_powers())

if __name__ == '__main__':
    main()
            