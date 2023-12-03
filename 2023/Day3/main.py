from Engine import Engine 

def main():
    engine = Engine('input.txt')
    print(f'{engine.sum_of_part_numbers()}')
    print(f'{engine.sum_of_gear_ratios()}')
    
if __name__ == '__main__':
    main()
            