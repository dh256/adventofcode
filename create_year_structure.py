import os

year = 2022
days = 25

for i in range(1,days+1):
    os.makedirs(f'{year}/Day{i}')
    os.chdir(f'{year}/Day{i}')
    with open(f'day{i}.py','w') as new_file:
        pass
    os.makedirs(f'tests')
    os.chdir('tests')
    with open(f'__init__.py','w') as  new_file2:
        pass
    with open(f'test_day{i}.py','w') as new_file3:
        pass
    os.chdir('../..')