# Assumption, x range is +ve and y range is -ve
import re
from collections import namedtuple

TargetRange = namedtuple('TargetRange','start end')

class Probe:
    def __init__(self, filename):
        with open(filename,'r') as input_file:
            nums = [int(num) for num in re.findall(r'-?\d+', input_file.readline().strip('\n'))]
            self.x_range = TargetRange(nums[0],nums[1])
            self.y_range = TargetRange(nums[2],nums[3])

    def highest_y(self):
        i_vels_hit_target = set()
        highest_ever_y = 0
        for ix_vel in range(1,self.x_range.end+1):                        # what is the range of initial x_vel - if outside a certain range will never hit target?
            for iy_vel in range(self.y_range.start,self.x_range.end+1):   # what is the range of initial y_vel - if outside a certain range will never hit target?
                highest_y = 0
                x, y = 0, 0
                x_vel, y_vel = ix_vel, iy_vel    
                while not (x > self.x_range.end or y < self.y_range.start):    # not overshot
                    x += x_vel
                    y += y_vel
                    highest_y = y if y > highest_y else highest_y
                    if self.x_range.start <= x <= self.x_range.end and self.y_range.start <= y <= self.y_range.end:
                        # Target Hit
                        highest_ever_y = highest_y if highest_y > highest_ever_y else highest_ever_y      
                        i_vels_hit_target.add((ix_vel,iy_vel))
                        break
                    else:
                        x_vel = x_vel-1 if x_vel > 0 else 0
                        y_vel -= 1 
                
        return highest_ever_y, len(i_vels_hit_target)
