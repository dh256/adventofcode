from Asteroid import AsteroidField
from Point2D import Point2D

from Line import Line

'''
line = Line(Point2D(3,4),Point2D(1,0))
on_line = line.point_on_line(Point2D(2,2))
print(on_line)
'''

field = AsteroidField("input.txt")
field.find_best_asteroid()
print(f'PART 1: Best Asteroid Can See: {field.best_asteroid_can_see}')
field.angle_to_best_asteroid()
answer = field.vapourize(200)
print(f'PART 2: {answer}')

'''
PART 2: For each asteroid in field work out angle to laser

field.best_asteroid = best_asteroid[0]
field.angle_to_best_asteroid()
field.vapourize(200)
'''

