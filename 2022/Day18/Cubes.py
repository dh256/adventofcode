from dataclasses import dataclass, field

@dataclass
class Point3D:
    x: int
    y: int
    z: int
        
    def transform(self,diff_x,diff_y,diff_z):
        return Point3D(self.x+diff_x, self.y+diff_y, self.z+diff_z)
        

class Cubes:
    transforms = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    def __init__(self, filename: str):
        self.cubes: list(Point3D) = list()
        with open(filename,'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
            for line in lines:
                points = line.split(',')
                self.cubes.append(Point3D(int(points[0]),int(points[1]),int(points[2])))

    def calc_surface_area(self) -> int:
        '''
        Return the number of sides of all cubes in grid whose faces is not covered by any other cube
        '''
        surface_area = 0
        for cube in self.cubes:
            for transform in Cubes.transforms:
                if not cube.transform(transform[0],transform[1],transform[2]) in self.cubes:
                    surface_area += 1

        return surface_area
        