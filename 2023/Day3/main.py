from Engine import Engine 
from Engine import Point

def main():
    engine = Engine('input.txt')
    print(f'{engine.sum_of_part_numbers()}')
    print(f'{engine.sum_of_gear_ratios()}')
    
if __name__ == '__main__':
    main()
            