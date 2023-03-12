from Cubes import Cubes

def main():
    cubes = Cubes('day18.txt')
    print(f'{cubes.calc_surface_area()}')

if __name__ == '__main__':
    main()