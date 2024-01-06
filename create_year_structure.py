import os
import argparse
import json

def create_class(day: int) -> None:
    with open(f'Day{day}.py', 'w') as day_file:
        day_file.write(f"""
class Day{day}:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            pass
            
    def part1(self) -> int:
        return 0

    def part2(self) -> int:
        return 0
                        
""")

def create_tests(day: int) -> None:
    os.chdir('..')
    os.makedirs(f'tests')
    os.chdir('tests')
    with open(f'__init__.py','w') as  _:
        pass
    with open(f'test_day{day}.py','w') as test_file:
        test_file.write(f"""
import pytest
from Day{day} import Day{day}

test_data1=[('tests/input.txt',0)]
test_data2=[('tests/input.txt',0)]
                  
@pytest.mark.parametrize('file_name,result',test_data1)
def test_part1(file_name,result):
    d = Day{day}(file_name)
    assert(d.part1() == result)

@pytest.mark.parametrize('file_name,result',test_data2)
def test_part2(file_name,result):
    d = Day{day}(file_name)
    assert(d.part2() == result)

""")
        
    with open(f'input.txt','w') as _:
        pass

def create_vscode(day: int) -> None:
    # create .vscode launch.json file (for debugging)
    configs: list[dict] = list()
    config: dict = dict()
    config['name'] = f'day{day}'
    config['type'] = 'python'
    config['request'] = 'launch'
    config['program'] = f'day_{day}.py'
    config['console'] = 'integratedTerminal'
    config['justMyCode'] = True
    configs.append(config)

    launch_json: dict = dict()
    launch_json['version'] = '0.2.0'
    launch_json['configurations'] = configs

    os.makedirs('.vscode')
    os.chdir('.vscode')
    with open('launch.json', 'w') as json_file:
        json.dump(launch_json, json_file)

def create_main_file(day: int) -> None:
    with open(f'day_{day}.py','w') as main_file:
        main_file.write(f""" 
from Day{day} import Day{day}
                            
def main():
    d = Day{day}('tests/input.txt')
    print(f'Part 1: {{d.part1()}}')
    #print(f'Part 2: {{d.part2()}}')

if __name__ == '__main__':
    main()
            """)

def main():
    # process command line args
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-y", type=int, dest="year", help="Year (e.g., 2023)")
    argParser.add_argument( "-d", type=int, dest="days", help="Number of Days (e.g., 25)")
    args = argParser.parse_args()
    year = args.year
    days = args.days

    # build directory structure
    os.makedirs(f'{year}')
    os.chdir(f'{year}')
    for day in range(1,days+1):
        # main Python file and input.txt file
        os.makedirs(f'Day{day}')
        os.chdir(f'Day{day}')
        
        # input.txt file
        with open(f'input.txt','w') as _:
            pass

        # create main file
        create_main_file(day)

        # create class
        create_class(day)

        # create .vscode
        create_vscode(day)

        # create tests
        create_tests(day)

        os.chdir('../..')

if __name__ == '__main__':
    main()