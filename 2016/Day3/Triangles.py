from itertools import permutations
import re

class Triangles:

    def __init__(self,filename):
        with open(filename,"r") as file_input:
            self.triangles = []
            lines=[line.strip('\n') for line in file_input]
            expr = re.compile('\d+')
            for line in lines:
                sides = [int(side) for side in expr.findall(line)]
                self.triangles.append(sides) 
            
    def possible(self,columns=False):
        possible_triangles = 0

        # part 1 work out combinations based on rows
        if not columns:
            possible_triangles = len([triangle for triangle in self.triangles if self.possible_triangle(triangle)])
        else:
            # Part 2: now need to read triangles in columns of 3
            # always check that we have a multiple of 3 rows
            if len(self.triangles) % 3 != 0:
                raise ValueError
            
            # calculcate number of groups of 3 rows
            row_groups = len(self.triangles) // 3

            # for each row group extract triangle in columns 0, 1 and 2
            for row_group in range(0,row_groups):
                for i in range(0,3):
                    triangle = [
                                    self.triangles[row_group * 3][i],
                                    self.triangles[row_group * 3+1][i],
                                    self.triangles[row_group * 3+2][i]
                    ]
                    
                    # determine if a possible triange            
                    if self.possible_triangle(triangle):
                        possible_triangles += 1

        return possible_triangles

    def possible_triangle(self, triangle):
        # get all combinations of sides for triangle 
        # for each combination add first two sides together and check less than third, if not, impossible return false
        # return true if all combinations possible
        perms = permutations(triangle)
        for perm in perms:
            if perm[0] + perm[1] <= perm[2]:
                return False   
        return True