from Springs import Springs 

def main():
    springs=Springs('input.txt')
    print(f'Part 1: {springs.condition_count_sum(1)}')

    springs=Springs('input.txt')
    print(f'Part 2: {springs.condition_count_sum(2)}')

if __name__ == '__main__':
    main()
            