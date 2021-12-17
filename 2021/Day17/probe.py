# Assumption, target lies to bottom left of start point i.e. x range is +ve and y range is -ve
import re

class Probe:
    def __init__(self, filename):
        with open(filename,'r') as input_file:
            nums = [int(num) for num in re.findall(r'-?\d+', input_file.readline().strip('\n'))]
            self.x_range = range(nums[0],nums[1])
            self.y_range = range(nums[2],nums[3])

    def fire(self):
        i_vels_hit_target = set()
        highest_ever_y = 0
        for ix_vel in range(1,self.x_range.stop+1):   # x_vel must be greater than 1 to move forward and <= x_range end to not overshoot target on first move 
            for iy_vel in range(self.y_range.start,self.x_range.stop+1):   # y_vel must be greater than y_range start to not overshoot on first move - if outside a certain range will never hit target, this is just an arbitrary no just now. Should be able to calculate this
                highest_y = 0
                x, y = 0, 0
                x_vel, y_vel = ix_vel, iy_vel    
                while not (x > self.x_range.stop or y < self.y_range.start):    # not overshot
                    # move probe by current velocity
                    x += x_vel
                    y += y_vel
                    highest_y = y if y > highest_y else highest_y
                    if self.x_range.start <= x <= self.x_range.stop and self.y_range.start <= y <= self.y_range.stop:
                        # Target Hit
                        highest_ever_y = highest_y if highest_y > highest_ever_y else highest_ever_y      
                        i_vels_hit_target.add((ix_vel,iy_vel))
                        break
                    else:
                        # change velocities
                        x_vel = x_vel-1 if x_vel > 0 else 0
                        y_vel -= 1 
                
        return highest_ever_y, len(i_vels_hit_target)

