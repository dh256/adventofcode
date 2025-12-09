from itertools import combinations
from shapely import Polygon, Point
class Day9:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            self._red_points: list[Point] = list()
            for line in input_file:
                x, y = map(lambda i: int(i), line.strip('\n').split(','))
                self._red_points.append(Point(x,y))

    def parts1and2(self) -> tuple[int,int]:
        
        # build green_area polygon
        green_area = Polygon(self._red_points + [self._red_points[0]])
        
        areas1: list[int] = list()
        areas2: list[int] = list()
        for corners in combinations(self._red_points,2):
            rect_area: int = int((abs(corners[0].x - corners[1].x)+1) * (abs(corners[0].y - corners[1].y)+1))
            
            # part 1 - add rectangle area
            areas1.append(rect_area)
            
            # part 2
            # build Polygon (rectangle) for all coordinate combinations
            # if rectangle is covered by green_area add to candidate areas
            corner2 = [corners[1].x,corners[0].y]
            corner4 = [corners[0].x,corners[1].y]
            rect = Polygon([corners[0],corner2,corners[1],corner4,corners[0]])
            if green_area.covers(rect):
                areas2.append(rect_area)
            
        return max(areas1), max(areas2)        
        
            
        
        
        
        
                        
