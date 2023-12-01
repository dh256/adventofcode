from WeatherMachine import WeatherMachine

def main():
    wm = WeatherMachine('input.txt')
    print(f'Part 1: {wm.sum_calibration_values(1)}')
    print(f'Part 2: {wm.sum_calibration_values(2)}')

if __name__ == '__main__':
    main()
            