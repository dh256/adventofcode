from Network import Network

def main():
    network = Network('input.txt')
    print(f'Part 1: {network.part_one()}')
    print(f'Part 2: {network.part_two()}')

if __name__ == '__main__':
    main()
            