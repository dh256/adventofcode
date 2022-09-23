from Tower import Tower

def main():
    tower = Tower('input.txt')
    print(f'{tower.root.id}')
    print(f'{tower.correct_weight_to_balance()}')

if __name__ == '__main__':
    main()