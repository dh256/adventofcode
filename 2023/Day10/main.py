from Pipes import Pipes

def main():
    pipes = Pipes('input.txt')
    print(f'Part 1: {pipes.steps_to_farthest()}')
    print(f'Part 2: {pipes.enclosed_by_loop()}')

if __name__ == '__main__':
    main()
            