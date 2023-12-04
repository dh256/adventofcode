from Cards import Cards 

def main():
    cards = Cards('input.txt')
    print(f'{cards.calc_points()}')
    print(f'{cards.calc_total_cards()}')

if __name__ == '__main__':
    main()
            