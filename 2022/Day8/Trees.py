class Trees:
    def __init__(self,file_name: str) -> None:
        self.trees = []
        with open(file_name,'r') as input_file:
            for line in [line.strip('\n') for line in input_file]:
                self.trees.append([int(c) for c in line])
        self.max_y = len(self.trees)-1
        self.max_x = len(self.trees[0])-1

    def number_visible(self) -> int:
        '''
        Return number of trees visible along any row/column from outside forest
        '''
        interior_visible = 0
        edge_visible = ((self.max_x+1) * 2) + ((self.max_y+1) * 2) - 4
        for x in range(1,self.max_x):
            for y in range(1,self.max_y):
                visible_left = True
                visible_right = True
                visible_up = True
                visible_down = True

                # look up from bottom
                for u in range(self.max_y,y,-1):
                    if self.trees[u][x] >= self.trees[y][x]:
                        visible_up = False
                        break

                # look down from top
                for d in range(0,y):
                    if self.trees[d][x] >= self.trees[y][x]:
                        visible_down = False
                        break
                
                # look along from the left 
                for l in range(0,x):
                    if self.trees[y][l] >= self.trees[y][x]:
                        visible_left = False
                        break

                # look along from right 
                for r in range(self.max_x,x,-1):
                    if self.trees[y][r] >= self.trees[y][x]:
                        visible_right = False
                        break
            
                if visible_right or visible_left or visible_up or visible_down:
                    interior_visible += 1

        return edge_visible + interior_visible

    def scenic_score(self) -> int:
        '''
        Calculate scenic score of each tree and return max
        '''
        scenic_scores = []
        # No need to do trees on edge as their scenic score is always 0
        for x in range(1,self.max_x):
            for y in range(1,self.max_y):
                curr_tree = self.trees[y][x]
                up_visible = 0
                down_visible = 0
                left_visible = 0
                right_visible = 0

                # trees up
                for u in range(y-1,-1,-1):
                    up_visible += 1
                    if self.trees[u][x] >= curr_tree:
                        break    

                # trees down
                for d in range(y+1,self.max_y+1):
                    down_visible += 1
                    if self.trees[d][x] >= curr_tree:
                        break
                    

                # trees left
                for l in range(x-1,-1,-1):
                    left_visible += 1
                    if self.trees[y][l] >= curr_tree:
                        break     

                # trees right
                for r in range(x+1,self.max_x+1):
                    right_visible += 1
                    if self.trees[y][r] >= curr_tree:
                        break

                scenic_scores.append(left_visible * right_visible * up_visible * down_visible)

        return max(scenic_scores)