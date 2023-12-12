from Springs import Springs 

def main():
    springs=Springs('input.txt')
    print(f'Part 1: {springs.condition_count_sum()}')

if __name__ == '__main__':
    main()
            